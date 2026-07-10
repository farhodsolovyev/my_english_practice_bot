"""Все клавиатуры в одном месте (DRY). Чистые функции → разметка.

callback_data строится через модуль `callbacks` — ни одной магической строки здесь.
"""
from __future__ import annotations

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

import callbacks as cb
from models import ListeningText, UserSettings
from settings_catalog import LEVEL_OPTIONS, TIME_OPTIONS, SIZE_OPTIONS, VOICE_OPTIONS


def _ikb(rows: list[list[InlineKeyboardButton]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=rows)


def _btn(text: str, data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=data)


_HOME = _btn("🏠 Меню", cb.MAIN_MENU)


# ─── Главное меню (Reply) ────────────────────────────────────────────────────
def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Тесты"), KeyboardButton(text="🎧 Аудирование")],
            [KeyboardButton(text="📊 Прогресс"), KeyboardButton(text="⚙️ Настройки")],
        ],
        resize_keyboard=True,
        persistent=True,
        input_field_placeholder="Выбери раздел 👇",
    )


def progress_kb(due: int) -> InlineKeyboardMarkup:
    rows = []
    if due:
        rows.append([_btn(f"🔁 Повторить ({due})", cb.quiz_pick("review"))])
    rows.append([_HOME])
    return _ikb(rows)


# ─── Подменю выбора теста ────────────────────────────────────────────────────
def tests_menu_kb(review_due: int = 0) -> InlineKeyboardMarkup:
    review_label = f"🔁 Повторение ({review_due})" if review_due else "🔁 Повторение"
    return _ikb([
        [_btn("📖 Слова", cb.quiz_pick("vocabulary")), _btn("🔄 Глаголы", cb.quiz_pick("verbs"))],
        [_btn("✍️ Предложения", cb.quiz_pick("sentences"))],
        [_btn(review_label, cb.quiz_pick("review"))],
        [_HOME],
    ])


# ─── Тест ────────────────────────────────────────────────────────────────────
STOP_TEXT = "⏹ Остановить тест"


def quiz_options_kb(qid: int, options: list[str]) -> InlineKeyboardMarkup:
    return _ikb([[_btn(opt, cb.answer(qid, idx))] for idx, opt in enumerate(options)])


def quiz_reveal_kb(options: list[str], correct: int, chosen: int | None,
                   option_notes: list | None = None) -> InlineKeyboardMarkup:
    """Кнопки-итог: ✅ у правильного, ❌ у ошибочно выбранного. Остаются в чате.

    option_notes (если есть) добавляет перевод к каждому варианту: «song — песня».
    """
    rows = []
    for idx, opt in enumerate(options):
        prefix = "✅ " if idx == correct else ("❌ " if idx == chosen else "▫️ ")
        label = prefix + opt
        if option_notes and option_notes[idx]:
            label += f" — {option_notes[idx]}"
        rows.append([_btn(label, cb.NOOP)])
    return _ikb(rows)


def test_stop_kb() -> ReplyKeyboardMarkup:
    """Нижняя панель во время теста — только остановка."""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=STOP_TEXT)]],
        resize_keyboard=True,
        input_field_placeholder="Отвечай кнопками в сообщениях 👆",
    )


# ─── Аудирование ─────────────────────────────────────────────────────────────
# Выбор уровня и текста — inline. Управление — в нижней панели (reply).
LST_SLOW, LST_NORM, LST_FAST = "🐢 Медленно", "🚶 Нормально", "🏃 Быстро"
LST_PREV, LST_NEXT = "⬅️ Пред. текст", "➡️ След. текст"
LST_TR = "📝 Перевод"
MENU_TEXT = "🏠 Меню"


def listen_levels_kb(levels: list[str]) -> InlineKeyboardMarkup:
    row = [_btn(lvl, cb.listen_level(lvl)) for lvl in levels]
    return _ikb([row, [_HOME]])


def listen_texts_kb(texts: list[ListeningText]) -> InlineKeyboardMarkup:
    rows = [[_btn(f"📄 {t.title}", cb.listen_open(t.id))] for t in texts]
    rows.append([_btn("◀️ Уровни", cb.LISTEN_LEVELS), _HOME])
    return _ikb(rows)


def listen_controls_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=LST_SLOW), KeyboardButton(text=LST_NORM), KeyboardButton(text=LST_FAST)],
            [KeyboardButton(text=LST_PREV), KeyboardButton(text=LST_NEXT)],
            [KeyboardButton(text=LST_TR), KeyboardButton(text=MENU_TEXT)],
        ],
        resize_keyboard=True,
        input_field_placeholder="Слушай и листай тексты 👇",
    )


# ─── Настройки ───────────────────────────────────────────────────────────────
def settings_menu_kb() -> InlineKeyboardMarkup:
    return _ikb([
        [_btn("🎚 Сложность", cb.setting_open("level")), _btn("⏱ Время", cb.setting_open("time"))],
        [_btn("🔢 Вопросов", cb.setting_open("size")), _btn("🔊 Голос", cb.setting_open("voice"))],
        [_HOME],
    ])


def _chooser(options: list[tuple], current, field: str, per_row: int = 2) -> InlineKeyboardMarkup:
    rows, row = [], []
    for value, lbl in options:
        mark = "✅ " if value == current else ""
        vstr = "none" if value is None else value
        row.append(_btn(mark + lbl, cb.setting_apply(field, vstr)))
        if len(row) == per_row:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([_btn("◀️ Назад", cb.SETTINGS_MENU)])
    return _ikb(rows)


def settings_level_kb(s: UserSettings) -> InlineKeyboardMarkup:
    return _chooser(LEVEL_OPTIONS, s.level, "level", per_row=3)


def settings_time_kb(s: UserSettings) -> InlineKeyboardMarkup:
    return _chooser(TIME_OPTIONS, s.quiz_seconds, "time", per_row=2)


def settings_size_kb(s: UserSettings) -> InlineKeyboardMarkup:
    return _chooser(SIZE_OPTIONS, s.quiz_size, "size", per_row=3)


def settings_voice_kb(s: UserSettings) -> InlineKeyboardMarkup:
    return _chooser(VOICE_OPTIONS, s.voice, "voice", per_row=2)


# ─── Адаптив: предложение сменить уровень после теста ────────────────────────
def level_suggestion_kb(direction: str, target: str, current: str | None) -> InlineKeyboardMarkup:
    if direction == "up":
        main = _btn(f"⬆️ Повысить до {target}", cb.level_set(target))
    else:
        main = _btn(f"⬇️ Понизить до {target}", cb.level_set(target))
    return _ikb([[main], [_btn(f"Оставить {current}", cb.LEVEL_KEEP)]])
