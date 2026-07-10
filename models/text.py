from dataclasses import dataclass

from models.level import Level


@dataclass(frozen=True)
class ListeningText:
    id: int
    title: str
    content: str
    translation: str
    level: Level = Level.A1

    @classmethod
    def from_dict(cls, data: dict) -> "ListeningText":
        return cls(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            translation=data["translation"],
            level=Level(data.get("level", "A1")),
        )
