from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Sentence:
    id: int
    text: str            # с символом «_» на месте пропуска
    answer: str          # правильное слово
    translation: str | None = None

    @property
    def blanked(self) -> str:
        """Текст с видимым пропуском для показа пользователю."""
        return self.text.replace("_", "_____")

    @classmethod
    def from_dict(cls, data: dict) -> "Sentence":
        return cls(
            id=data["id"],
            text=data["text"],
            answer=data["answer"],
            translation=data.get("translation"),
        )
