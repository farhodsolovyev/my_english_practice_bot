from __future__ import annotations

from models import ListeningText
from repositories.base import AbstractTextRepository


class PyFileTextRepository(AbstractTextRepository):
    def __init__(self, source: list[dict]):
        self._texts: list[ListeningText] = [ListeningText.from_dict(row) for row in source]
        self._by_id: dict[int, ListeningText] = {t.id: t for t in self._texts}

    async def get_all(self) -> list[ListeningText]:
        return list(self._texts)

    async def get_by_id(self, text_id: int) -> ListeningText | None:
        return self._by_id.get(text_id)
