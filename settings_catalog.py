"""Каталог настроек: допустимые значения + человекочитаемые подписи.

Нейтральный справочник (как config): им пользуются и слой представления
(keyboards/presenters — для кнопок и отображения), и сервис (для валидации).
Так presentation не зависит от service.
"""
from __future__ import annotations

# (значение, подпись)
LEVEL_OPTIONS = [(None, "🌍 Все"), ("A1", "A1"), ("A2", "A2"), ("B1", "B1"), ("B2", "B2")]
TIME_OPTIONS = [(10, "⚡ 10 сек"), (15, "🚶 15 сек"), (25, "🐢 25 сек"), (0, "∞ Без таймера")]
SIZE_OPTIONS = [(5, "5"), (10, "10"), (15, "15")]
VOICE_OPTIONS = [
    ("en-US-AriaNeural", "🇺🇸 Женский"),
    ("en-US-GuyNeural", "🇺🇸 Мужской"),
    ("en-GB-SoniaNeural", "🇬🇧 Женский"),
    ("en-GB-RyanNeural", "🇬🇧 Мужской"),
]


def label_for(options: list[tuple], value) -> str:
    for v, lbl in options:
        if v == value:
            return lbl
    return str(value)
