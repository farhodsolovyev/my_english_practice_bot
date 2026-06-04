"""
English Learning Bot — стартовый шаблон
Три блока:
  1) Словарный запас — карточки с интервальными повторениями (метод Лейтнера)
  2) Грамматика — мини-уроки + квизы
  3) Разговорная практика — диалог с ИИ, который мягко исправляет ошибки

Стек: python-telegram-bot v20+ (async), SQLite (встроена), httpx (для ИИ).
Python 3.10+

Запуск:
  export BOT_TOKEN="токен_от_BotFather"
  export ANTHROPIC_API_KEY="ключ_anthropic"   # нужен только для блока «Разговор»
  python bot.py
"""

import os
import sqlite3
import datetime as dt
from contextlib import closing

import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ---------- НАСТРОЙКИ ----------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8922540867:AAF-1dQYi929S8EBpPH-CuDjvGob8zwDrLA")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
# Проверь актуальное имя модели в docs.anthropic.com. Haiku — дешевле, Sonnet — умнее.
MODEL = "claude-haiku-4-5-20251001"
DB_PATH = "english_bot.db"
REMINDER_HOUR = 19  # во сколько (по времени сервера) присылать ежедневное напоминание

# Интервалы повторений в днях по «коробкам» Лейтнера:
# угадал -> слово переходит в следующую коробку (интервал растёт),
# ошибся -> возвращается в коробку 1.
LEITNER_INTERVALS = {1: 1, 2: 3, 3: 7, 4: 16, 5: 35}

# ---------- БАЗОВЫЙ НАБОР СЛОВ (расширяй сам: слово, перевод, пример) ----------
WORD_BANK = [
    ("appointment", "встреча, приём", "I have a doctor's appointment at 3 PM."),
    ("reliable", "надёжный", "She is a reliable colleague you can count on."),
    ("schedule", "расписание / планировать", "Let's schedule a call for tomorrow."),
    ("afford", "позволить себе", "I can't afford a new car right now."),
    ("improve", "улучшать", "I want to improve my speaking skills."),
    ("available", "доступный, свободный", "Are you available on Friday?"),
    ("suggest", "предлагать", "Can you suggest a good restaurant?"),
    ("deadline", "крайний срок", "The deadline for the report is Monday."),
    ("decision", "решение", "It was a difficult decision to make."),
    ("opportunity", "возможность", "This job is a great opportunity for me."),
]

# ---------- ГРАММАТИКА: мини-уроки + квизы ----------
# Формат вопроса: (предложение с ___, [варианты], индекс правильного варианта)
GRAMMAR = [
    {
        "title": "Present Simple vs Present Continuous",
        "lesson": (
            "Present Simple — регулярные действия и факты: I work every day.\n"
            "Present Continuous — действие прямо сейчас / временное: I am working now.\n"
            "Маркеры Simple: usually, every day, often. Маркеры Continuous: now, at the moment."
        ),
        "quiz": [
            ("I ___ coffee every morning.", ["drink", "am drinking"], 0),
            ("Look! It ___ outside.", ["rains", "is raining"], 1),
            ("She ___ in a bank.", ["works", "is working"], 0),
        ],
    },
    {
        "title": "Articles: a / an / the",
        "lesson": (
            "a/an — что-то одно, упомянутое впервые: I saw a dog.\n"
            "the — конкретное, уже известное: The dog was black.\n"
            "an — перед гласным звуком: an apple, an hour."
        ),
        "quiz": [
            ("I need ___ umbrella.", ["a", "an"], 1),
            ("She is ___ best student in class.", ["a", "the"], 1),
            ("He bought ___ car yesterday.", ["a", "the"], 0),
        ],
    },
]

SYSTEM_PROMPT = (
    "You are a friendly English conversation tutor for a Russian-speaking learner. "
    "Continue the conversation with simple, natural English. After each learner message: "
    "(1) reply naturally to keep the dialogue going; "
    "(2) if there are mistakes, gently show a corrected version and a more natural phrasing; "
    "(3) end with a short question to keep them talking. Keep replies brief."
)


# ---------- БАЗА ДАННЫХ ----------
def db():
    return sqlite3.connect(DB_PATH)


def init_db():
    with closing(db()) as conn, conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS cards(
                user_id INTEGER, word TEXT, translation TEXT, example TEXT,
                box INTEGER DEFAULT 1, next_review TEXT,
                PRIMARY KEY (user_id, word))"""
        )


def ensure_cards(user_id: int):
    """Заводит карточки слов для нового пользователя (один раз)."""
    today = dt.date.today().isoformat()
    with closing(db()) as conn, conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM cards WHERE user_id=?", (user_id,)
        ).fetchone()[0]
        if count == 0:
            for w, t, e in WORD_BANK:
                conn.execute(
                    "INSERT OR IGNORE INTO cards(user_id, word, translation, example, box, next_review) "
                    "VALUES (?,?,?,?,1,?)",
                    (user_id, w, t, e, today),
                )


def get_due_card(user_id: int):
    """Возвращает одно слово, которое пора повторить (или None)."""
    today = dt.date.today().isoformat()
    with closing(db()) as conn:
        return conn.execute(
            "SELECT word, translation, example, box FROM cards "
            "WHERE user_id=? AND next_review<=? ORDER BY next_review LIMIT 1",
            (user_id, today),
        ).fetchone()


def get_card(user_id: int, word: str):
    with closing(db()) as conn:
        return conn.execute(
            "SELECT word, translation, example, box FROM cards WHERE user_id=? AND word=?",
            (user_id, word),
        ).fetchone()


def update_card(user_id: int, word: str, correct: bool):
    with closing(db()) as conn, conn:
        row = conn.execute(
            "SELECT box FROM cards WHERE user_id=? AND word=?", (user_id, word)
        ).fetchone()
        box = row[0] if row else 1
        box = min(box + 1, 5) if correct else 1
        nxt = (dt.date.today() + dt.timedelta(days=LEITNER_INTERVALS[box])).isoformat()
        conn.execute(
            "UPDATE cards SET box=?, next_review=? WHERE user_id=? AND word=?",
            (box, nxt, user_id, word),
        )


# ---------- ИНТЕРФЕЙС ----------
def main_menu():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📚 Слова (повторение)", callback_data="vocab")],
            [InlineKeyboardButton("✍️ Грамматика", callback_data="grammar")],
            [InlineKeyboardButton("💬 Разговор с ИИ", callback_data="chat")],
        ]
    )


async def send_card(query, user_id: int):
    card = get_due_card(user_id)
    if not card:
        await query.edit_message_text(
            "🎉 На сегодня все слова повторены! Возвращайся завтра.", reply_markup=main_menu()
        )
        return
    word, tr, ex, box = card
    kb = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("👀 Показать ответ", callback_data=f"rv|{word}")],
            [InlineKeyboardButton("⬅️ Меню", callback_data="menu")],
        ]
    )
    await query.edit_message_text(f"Как сказать по-английски?\n\n*{tr}*", reply_markup=kb, parse_mode="Markdown")


async def send_grammar_lesson(query, idx: int):
    lesson = GRAMMAR[idx]
    kb = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("▶️ Начать квиз", callback_data=f"gq|{idx}|0")],
            [InlineKeyboardButton("⬅️ Меню", callback_data="menu")],
        ]
    )
    await query.edit_message_text(
        f"*{lesson['title']}*\n\n{lesson['lesson']}", reply_markup=kb, parse_mode="Markdown"
    )


async def send_question(query, li: int, qi: int):
    quiz = GRAMMAR[li]["quiz"]
    if qi >= len(quiz):
        await query.edit_message_text("✅ Квиз пройден! Отличная работа.", reply_markup=main_menu())
        return
    q, options, _ = quiz[qi]
    buttons = [InlineKeyboardButton(opt, callback_data=f"ga|{li}|{qi}|{i}") for i, opt in enumerate(options)]
    await query.edit_message_text(f"Вопрос {qi + 1}:\n\n{q}", reply_markup=InlineKeyboardMarkup([buttons]))


# ---------- ИИ ДЛЯ РАЗГОВОРНОЙ ПРАКТИКИ ----------
async def ask_llm(history: list) -> str:
    if not ANTHROPIC_API_KEY:
        return "⚠️ Не задан ANTHROPIC_API_KEY. Добавь ключ, чтобы включить разговорную практику."
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json={
                    "model": MODEL,
                    "max_tokens": 500,
                    "system": SYSTEM_PROMPT,
                    "messages": history,
                },
            )
        data = r.json()
        return data["content"][0]["text"]
    except Exception as e:
        return f"Не получилось получить ответ ИИ: {e}"


# ---------- ХЕНДЛЕРЫ ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ensure_cards(user.id)

    # ежедневное напоминание (требует python-telegram-bot[job-queue])
    if context.job_queue:
        chat_id = update.effective_chat.id
        for j in context.job_queue.get_jobs_by_name(str(chat_id)):
            j.schedule_removal()
        context.job_queue.run_daily(
            daily_reminder,
            time=dt.time(hour=REMINDER_HOUR, minute=0),
            chat_id=chat_id,
            name=str(chat_id),
        )

    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n"
        "Я помогу учить английский: слова, грамматика и разговорная практика.\n"
        "Выбери, с чего начать:",
        reply_markup=main_menu(),
    )


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = None
    await update.message.reply_text("Вышел из режима разговора.", reply_markup=main_menu())


async def daily_reminder(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context.job.chat_id, "⏰ Время для английского! Открой меню: /start")


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data == "menu":
        await query.edit_message_text("Главное меню:", reply_markup=main_menu())

    elif data == "vocab":
        await send_card(query, user_id)

    elif data.startswith("rv|"):  # показать ответ
        word = data.split("|", 1)[1]
        card = get_card(user_id, word)
        if not card:
            await send_card(query, user_id)
            return
        word, tr, ex, box = card
        kb = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("✅ Помню", callback_data=f"ok|{word}"),
                InlineKeyboardButton("❌ Забыл", callback_data=f"no|{word}"),
            ]]
        )
        await query.edit_message_text(f"*{word}* — {tr}\n\n_{ex}_\n\nТы вспомнил?", reply_markup=kb, parse_mode="Markdown")

    elif data.startswith("ok|") or data.startswith("no|"):
        word = data.split("|", 1)[1]
        update_card(user_id, word, data.startswith("ok|"))
        await send_card(query, user_id)

    elif data == "grammar":
        await send_grammar_lesson(query, 0)

    elif data.startswith("gq|"):  # старт/следующий вопрос квиза
        _, li, qi = data.split("|")
        await send_question(query, int(li), int(qi))

    elif data.startswith("ga|"):  # ответ на вопрос квиза
        _, li, qi, choice = data.split("|")
        li, qi, choice = int(li), int(qi), int(choice)
        q, options, correct = GRAMMAR[li]["quiz"][qi]
        filled = q.replace("___", options[correct])
        fb = f"✅ Верно! {filled}" if choice == correct else f"❌ Не совсем. Правильно: {filled}"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("➡️ Дальше", callback_data=f"gq|{li}|{qi + 1}")]])
        await query.edit_message_text(fb, reply_markup=kb)

    elif data == "chat":
        context.user_data["mode"] = "chat"
        context.user_data["history"] = []
        await query.edit_message_text(
            "💬 Режим разговора включён. Пиши мне на английском — я отвечу и поправлю ошибки.\n"
            "Напиши /stop, чтобы выйти."
        )


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("mode") != "chat":
        await update.message.reply_text("Нажми /start, чтобы открыть меню.")
        return
    history = context.user_data.setdefault("history", [])
    history.append({"role": "user", "content": update.message.text})
    await context.bot.send_chat_action(update.effective_chat.id, "typing")
    reply = await ask_llm(history)
    history.append({"role": "assistant", "content": reply})
    await update.message.reply_text(reply)


def main():
    if not BOT_TOKEN:
        raise SystemExit("Задай переменную окружения BOT_TOKEN (токен от BotFather).")
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    print("Бот запущен. Останови через Ctrl+C.")
    app.run_polling()


if __name__ == "__main__":
    main()
