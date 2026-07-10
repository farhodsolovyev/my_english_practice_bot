"""Единый поток теста: слова / глаголы / предложения.

Хендлер занимается только Telegram-I/O (отправка/правка сообщений, таймер).
Вся чистая логика (что верно, когда следующий, счёт, %) — в модели QuizSession.

UX: каждый вопрос отдельным сообщением (остаётся в чате), авто-переход,
дедлайн с авто-провалом (0 в настройках → без таймера), кнопка «Стоп» в панели.
"""
from __future__ import annotations

import asyncio
import logging

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import callbacks as cb
from config import settings
from containers import Container
from models import QuizSession
from keyboards.main_kb import (
    quiz_options_kb, quiz_reveal_kb, tests_menu_kb, test_stop_kb, main_menu_kb,
    level_suggestion_kb, STOP_TEXT,
)
from handlers.utils import safe_edit_by_id

router = Router()
logger = logging.getLogger(__name__)

_SECTION_TITLE = {
    "vocabulary": "📖 Слова",
    "verbs": "🔄 Глаголы",
    "sentences": "✍️ Предложения",
    "review": "🔁 Повторение",
}


def _load(data: dict) -> QuizSession | None:
    raw = data.get("quiz")
    return QuizSession.from_dict(raw) if raw else None


async def _save(state: FSMContext, session: QuizSession) -> None:
    await state.update_data(quiz=session.to_dict())


# ─── Подменю «Тесты» ─────────────────────────────────────────────────────────
@router.message(F.text == "📝 Тесты")
async def tests_menu(message: Message, container: Container) -> None:
    due = len(await container.srs.due_ids(message.from_user.id))
    await message.answer("📝 <b>Выбери тест:</b>", reply_markup=tests_menu_kb(due))


@router.callback_query(F.data.startswith(cb.QUIZ_PICK))
async def pick_quiz(callback: CallbackQuery, state: FSMContext, bot: Bot, container: Container) -> None:
    section = cb.parse_quiz_pick(callback.data)
    await callback.answer()
    await start_quiz(bot, state, container, callback.message.chat.id, callback.from_user.id, section)


# ─── Запуск теста ────────────────────────────────────────────────────────────
async def start_quiz(
    bot: Bot, state: FSMContext, container: Container, chat_id: int, user_id: int, section: str
) -> None:
    us = await container.settings.get(user_id)
    level = us.level

    if section == "review":
        pool = await container.vocabulary.quiz_items(None)   # все слова — пул дистракторов
        due = set(await container.srs.due_ids(user_id))
        ask = [it for it in pool if it.ref in due]
        if not ask:
            await bot.send_message(
                chat_id,
                "🎉 Пока нечего повторять!\n"
                "Пройди «📖 Слова» — и они начнут возвращаться к повторению по расписанию.",
            )
            return
        questions = container.quiz.build(pool, us.quiz_size, settings.quiz_options, ask_from=ask)
        level = None
    else:
        items = await _items_for(container, section, us.level)
        questions = container.quiz.build(items, us.quiz_size, settings.quiz_options)

    if not questions:
        await bot.send_message(chat_id, "❌ Недостаточно данных для теста.")
        return

    session = QuizSession(
        section=section, user_id=user_id, chat_id=chat_id,
        questions=questions, level=level, deadline=us.quiz_seconds,
    )
    await _save(state, session)
    # Нижняя панель на «Стоп» (варианты ответа — inline в сообщениях).
    await bot.send_message(
        chat_id,
        "🎯 <b>Поехали!</b> Отвечай кнопками в сообщениях.\n<i>Остановить — кнопкой снизу.</i>",
        reply_markup=test_stop_kb(),
    )
    await _send_question(bot, state, container, session)


async def _items_for(container: Container, section: str, level: str | None):
    if section == "verbs":
        return await container.verbs.quiz_items()
    if section == "sentences":
        return await container.sentences.quiz_items()
    return await container.vocabulary.quiz_items(level)


# ─── Рендер вопроса (новым сообщением) ───────────────────────────────────────
def _question_text(session: QuizSession, index: int) -> str:
    q = session.questions[index]
    title = _SECTION_TITLE.get(session.section, "❓ Тест")
    timer = f"   ⏱ {session.deadline} сек" if session.deadline else ""
    return f"{title} · вопрос <b>{index + 1}/{session.total}</b>{timer}\n\n{q.prompt}"


async def _send_question(bot: Bot, state: FSMContext, container: Container, session: QuizSession) -> None:
    q = session.current
    sent = await bot.send_message(
        session.chat_id, _question_text(session, session.i),
        reply_markup=quiz_options_kb(session.qid, q.options),
    )
    session.msg_id = sent.message_id
    await _save(state, session)
    if session.deadline:
        _spawn_timer(bot, state, container, session.qid, session.deadline)


# ─── Таймер дедлайна ─────────────────────────────────────────────────────────
def _spawn_timer(bot: Bot, state: FSMContext, container: Container, qid: int, deadline: int) -> None:
    asyncio.create_task(_deadline(bot, state, container, qid, deadline))


async def _deadline(bot: Bot, state: FSMContext, container: Container, qid: int, deadline: int) -> None:
    try:
        await asyncio.sleep(deadline)
        session = _load(await state.get_data())
        if not session or session.qid != qid:
            return  # уже ответили / сессия сменилась
        await _reveal_and_advance(bot, state, container, chosen=None)
    except asyncio.CancelledError:
        raise
    except Exception:
        logger.exception("Сбой таймера теста")


# ─── Ответ / таймаут → пометка сообщения + следующий вопрос ──────────────────
async def _reveal_and_advance(
    bot: Bot, state: FSMContext, container: Container, chosen: int | None
) -> None:
    session = _load(await state.get_data())
    if not session:
        return

    index = session.i
    q = session.current
    prev_msg_id = session.msg_id
    is_correct = session.check(chosen)
    session.register(is_correct)
    session.advance()
    await _save(state, session)

    # Копим статистику по уровню — только тест слов (адаптив сложности).
    if session.section == "vocabulary":
        try:
            await container.stats.record(session.user_id, session.level, is_correct)
        except Exception:
            logger.exception("Не удалось записать статистику")

    # Интервальное повторение — для любого вопроса со ссылкой на слово (тест слов и повторение).
    if q.ref is not None:
        try:
            await container.srs.review(session.user_id, q.ref, is_correct)
        except Exception:
            logger.exception("Не удалось обновить SRS")

    # Дневная активность (серия/цель) — любой ответ считается практикой.
    try:
        await container.progress.record(session.user_id)
    except Exception:
        logger.exception("Не удалось записать активность")

    # Помечаем отвеченное сообщение (оно остаётся в чате).
    if chosen is None:
        verdict = "⏱ <b>Время вышло!</b>"
    elif is_correct:
        verdict = "✅ <b>Верно!</b>"
    else:
        verdict = "❌ <b>Неверно.</b>"
    reveal_text = _question_text(session, index) + f"\n\n{verdict}"
    if q.note:
        reveal_text += f"\n\n💬 {q.note}"
    await safe_edit_by_id(bot, session.chat_id, prev_msg_id, reveal_text,
                          quiz_reveal_kb(q.options, q.correct, chosen, q.option_notes))

    if session.is_finished:
        await _finish(bot, state, container, session)
    else:
        await _send_question(bot, state, container, session)


async def _finish(bot: Bot, state: FSMContext, container: Container, session: QuizSession, stopped: bool = False) -> None:
    c, w, pct = session.correct, session.wrong, session.percent
    total = c + w
    if stopped:
        head = "⏹ <b>Тест остановлен</b>"
    else:
        emoji = "🏆" if pct >= 80 else "👍" if pct >= 50 else "📚"
        head = f"{emoji} <b>Тест завершён!</b>"
    text = (
        f"{head}  ({_SECTION_TITLE.get(session.section, '')})\n\n"
        f"✅ Верно: {c}/{total}\n"
        f"❌ Ошибок: {w}/{total}\n"
        f"📊 Результат: <b>{pct}%</b>\n\n"
        f"<i>Прокрути вверх, чтобы разобрать ошибки.</i>"
    )
    await state.update_data(quiz=None, last_section=session.section)
    await bot.send_message(session.chat_id, text, reply_markup=main_menu_kb())

    # Адаптив: по итогам теста слов предложить сменить уровень.
    if not stopped and session.section == "vocabulary":
        try:
            sug = await container.stats.suggestion(session.user_id, session.level)
        except Exception:
            sug = None
        if sug:
            direction, target, acc = sug
            if direction == "up":
                msg = f"🚀 <b>Отлично — {acc}% верно!</b>\nГотов усложнить слова?"
            else:
                msg = f"🙂 <b>Пока сложновато ({acc}%).</b>\nПопробуем уровень полегче?"
            await bot.send_message(
                session.chat_id, msg,
                reply_markup=level_suggestion_kb(direction, target, session.level),
            )


# ─── Колбэки ─────────────────────────────────────────────────────────────────
@router.callback_query(F.data.startswith(cb.ANSWER))
async def on_answer(callback: CallbackQuery, state: FSMContext, bot: Bot, container: Container) -> None:
    qid, chosen = cb.parse_answer(callback.data)
    session = _load(await state.get_data())
    if not session or session.qid != qid:
        await callback.answer("Этот вопрос уже закрыт ⏱")
        return
    correct = session.current.correct
    await callback.answer("✅ Верно!" if chosen == correct else "❌ Неверно")
    await _reveal_and_advance(bot, state, container, chosen)


@router.message(F.text == STOP_TEXT)
async def on_stop(message: Message, state: FSMContext, bot: Bot, container: Container) -> None:
    session = _load(await state.get_data())
    if not session:
        await message.answer("Активного теста нет 🙂", reply_markup=main_menu_kb())
        return
    await safe_edit_by_id(
        bot, session.chat_id, session.msg_id,
        _question_text(session, session.i) + "\n\n⏹ <i>Тест остановлен</i>", None,
    )
    session.qid += 1  # инвалидируем таймер текущего вопроса
    await _finish(bot, state, container, session, stopped=True)


@router.callback_query(F.data == cb.NOOP)
async def on_noop(callback: CallbackQuery) -> None:
    await callback.answer()
