from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListenState:
    """Текущий контекст аудирования (какой текст открыт и его уровень)."""
    text_id: int
    level: str

    def to_dict(self) -> dict:
        return {"text_id": self.text_id, "level": self.level}

    @classmethod
    def from_dict(cls, d: dict) -> "ListenState":
        return cls(text_id=d["text_id"], level=d["level"])
