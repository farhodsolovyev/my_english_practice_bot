from __future__ import annotations

from dataclasses import dataclass

DEFAULT_VOICE = "en-US-AriaNeural"


@dataclass
class UserSettings:
    """Пользовательские настройки. level=None → «Все уровни»; quiz_seconds=0 → без таймера.

    По умолчанию сложность A1 — нормальная прогрессия с лёгкого (адаптив ведёт выше).
    """
    user_id: int
    level: str | None = "A1"
    quiz_seconds: int = 15
    quiz_size: int = 10
    voice: str = DEFAULT_VOICE

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "level": self.level,
            "quiz_seconds": self.quiz_seconds,
            "quiz_size": self.quiz_size,
            "voice": self.voice,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "UserSettings":
        return cls(
            user_id=data["user_id"],
            level=data.get("level", "A1"),
            quiz_seconds=data.get("quiz_seconds", 15),
            quiz_size=data.get("quiz_size", 10),
            voice=data.get("voice", DEFAULT_VOICE),
        )
