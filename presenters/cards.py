"""Форматирование сообщений (View-слой). Чистые функции модель → HTML-строка."""
from __future__ import annotations

from models import ListeningText, UserSettings
from settings_catalog import (
    LEVEL_OPTIONS, TIME_OPTIONS, SIZE_OPTIONS, VOICE_OPTIONS, label_for,
)


def text_view(text: ListeningText) -> str:
    return (
        f"📄 <b>{text.title}</b>  [{text.level.value}]\n\n"
        f"{text.content}\n\n"
        f"<i>Выбери скорость снизу, листай тексты ⬅️ ➡️</i>"
    )


def progress_view(summary: dict, srs: dict, level: str | None) -> str:
    best = f" (рекорд {summary['best']})" if summary["best"] > summary["streak"] else ""
    return (
        "📊 <b>Твой прогресс</b>\n\n"
        f"🔥 Серия: <b>{summary['streak']}</b> дн.{best}\n"
        f"🎯 Сегодня: <b>{summary['today']}/{summary['goal']}</b> ответов\n"
        f"🎚 Уровень: <b>{level or 'Все'}</b>\n\n"
        f"📚 Слова: изучается <b>{srs['total']}</b> · выучено <b>{srs['learned']}</b>\n"
        f"🔁 К повторению сейчас: <b>{srs['due']}</b>"
    )


def settings_view(s: UserSettings) -> str:
    return (
        "⚙️ <b>Настройки</b>\n\n"
        f"🎚 Сложность: <b>{label_for(LEVEL_OPTIONS, s.level)}</b>\n"
        f"⏱ Время на ответ: <b>{label_for(TIME_OPTIONS, s.quiz_seconds)}</b>\n"
        f"🔢 Вопросов в тесте: <b>{label_for(SIZE_OPTIONS, s.quiz_size)}</b>\n"
        f"🔊 Голос озвучки: <b>{label_for(VOICE_OPTIONS, s.voice)}</b>\n\n"
        "<i>Выбери, что изменить 👇</i>"
    )
