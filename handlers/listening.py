from __future__ import annotations

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

import callbacks as cb
from containers import Container
from models import ListenState
from keyboards.main_kb import (
    listen_levels_kb, listen_texts_kb, listen_controls_kb,
    LST_SLOW, LST_NORM, LST_FAST, LST_PREV, LST_NEXT, LST_TR,
)
from presenters import text_view
from providers.tts import Speed
from handlers.utils import safe_edit

router = Router()

_SPEED_BY_TEXT = {LST_SLOW: Speed.SLOW, LST_NORM: Speed.NORMAL, LST_FAST: Speed.FAST}
_SPEED_LABEL = {Speed.SLOW: "🐢 Медленно", Speed.NORMAL: "🚶 Нормально", Speed.FAST: "🏃 Быстро"}
_NO_TEXT = "Сначала открой текст: 🎧 Аудирование."
_LEVELS_TITLE = "🎧 <b>Аудирование</b>\nВыбери уровень сложности:"


def _texts_title(level: str, count: int) -> str:
    return f"🎧 <b>Уровень {level}</b> — выбери текст ({count}):"


def _load(data: dict) -> ListenState | None:
    raw = data.get("listen")
    return ListenState.from_dict(raw) if raw else None


# ─── Выбор уровня и текста (inline в сообщениях) ─────────────────────────────
@router.message(F.text == "🎧 Аудирование")
async def open_listening(message: Message, container: Container) -> None:
    levels = await container.listening.levels()
    if not levels:
        await message.answer("❌ Тексты не найдены.")
        return
    await message.answer(_LEVELS_TITLE, reply_markup=listen_levels_kb(levels))


@router.callback_query(F.data == cb.LISTEN_LEVELS)
async def back_to_levels(callback: CallbackQuery, container: Container) -> None:
    levels = await container.listening.levels()
    await safe_edit(callback.message, _LEVELS_TITLE, listen_levels_kb(levels))
    await callback.answer()


@router.callback_query(F.data.startswith(cb.LISTEN_LEVEL))
async def choose_level(callback: CallbackQuery, container: Container) -> None:
    level = cb.parse_listen_level(callback.data)
    texts = await container.listening.by_level(level)
    await safe_edit(callback.message, _texts_title(level, len(texts)), listen_texts_kb(texts))
    await callback.answer()


@router.callback_query(F.data.startswith(cb.LISTEN_OPEN))
async def open_text(callback: CallbackQuery, state: FSMContext, container: Container) -> None:
    text = await container.listening.get(cb.parse_listen_open(callback.data))
    if not text:
        await callback.answer("Текст не найден", show_alert=True)
        return
    await state.update_data(listen=ListenState(text.id, text.level.value).to_dict())
    await callback.message.answer(text_view(text), reply_markup=listen_controls_kb())
    await callback.answer()


# ─── Управление прослушиванием (нижняя панель) ───────────────────────────────
@router.message(F.text.in_(set(_SPEED_BY_TEXT)))
async def play_text(message: Message, state: FSMContext, container: Container) -> None:
    listen = _load(await state.get_data())
    if not listen:
        await message.answer(_NO_TEXT)
        return
    text = await container.listening.get(listen.text_id)
    if not text:
        await message.answer(_NO_TEXT)
        return

    speed = _SPEED_BY_TEXT[message.text]
    voice = (await container.settings.get(message.from_user.id)).voice
    await message.answer(f"🔊 Генерирую… {_SPEED_LABEL[speed]}")
    try:
        path = await container.listening.audio(text, speed, voice)
        await message.answer_voice(FSInputFile(path), caption=f"🔊 <b>{text.title}</b> — {_SPEED_LABEL[speed]}")
    except Exception as e:
        await message.answer(f"❌ Ошибка аудио: {e}")


@router.message(F.text == LST_NEXT)
async def next_text(message: Message, state: FSMContext, container: Container) -> None:
    await _navigate(message, state, container, +1)


@router.message(F.text == LST_PREV)
async def prev_text(message: Message, state: FSMContext, container: Container) -> None:
    await _navigate(message, state, container, -1)


async def _navigate(message: Message, state: FSMContext, container: Container, delta: int) -> None:
    listen = _load(await state.get_data())
    if not listen:
        await message.answer(_NO_TEXT)
        return
    texts = await container.listening.by_level(listen.level)
    ids = [t.id for t in texts]
    idx = ids.index(listen.text_id) if listen.text_id in ids else 0
    text = texts[(idx + delta) % len(texts)]
    await state.update_data(listen=ListenState(text.id, listen.level).to_dict())
    await message.answer(text_view(text), reply_markup=listen_controls_kb())


@router.message(F.text == LST_TR)
async def show_translation(message: Message, state: FSMContext, container: Container) -> None:
    listen = _load(await state.get_data())
    if not listen:
        await message.answer(_NO_TEXT)
        return
    text = await container.listening.get(listen.text_id)
    await message.answer(f"📝 <b>Перевод: {text.title}</b>\n\n{text.translation}")
