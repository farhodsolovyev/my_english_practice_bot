from __future__ import annotations

from dataclasses import dataclass, field

from models.level import Level


@dataclass(frozen=True)
class WordMeaning:
    """Одно значение слова. Слово может иметь несколько значений."""
    russian: str
    example_en: str | None = None
    example_ru: str | None = None


@dataclass(frozen=True)
class Word:
    id: int
    english: str
    transcription: str | None = None      # IPA, напр. "skuːl"
    ru: str | None = None                  # русская транскрипция, напр. "скул"
    level: Level = Level.A1
    topic: str = "general"
    meanings: list[WordMeaning] = field(default_factory=list)
    # Словообразование (суффиксы/приставки) — точка расширения, логики пока нет.
    formation: str | None = None

    @property
    def primary_translation(self) -> str:
        """Основной перевод (первое значение) — для краткого показа и вариантов теста."""
        return self.meanings[0].russian if self.meanings else ""

    @classmethod
    def from_dict(cls, data: dict) -> "Word":
        return cls(
            id=data["id"],
            english=data["english"],
            transcription=data.get("transcription"),
            ru=data.get("ru"),
            level=Level(data.get("level", "A1")),
            topic=data.get("topic", "general"),
            meanings=[WordMeaning(**m) for m in data.get("meanings", [])],
            formation=data.get("formation"),
        )
