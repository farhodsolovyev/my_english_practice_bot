from __future__ import annotations

from models import Sentence
from repositories.base import AbstractSentenceRepository


class PyFileSentenceRepository(AbstractSentenceRepository):
    def __init__(self, source: list[dict]):
        self._items: list[Sentence] = [Sentence.from_dict(row) for row in source]

    async def get_all(self) -> list[Sentence]:
        return list(self._items)
