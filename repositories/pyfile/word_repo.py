from __future__ import annotations

import random

from models import Word
from repositories.base import AbstractWordRepository


class PyFileWordRepository(AbstractWordRepository):
    """Читает слова из .py-источника (list[dict]) и отдаёт доменные Word.

    Данные иммутабельны и грузятся один раз в память — для read-only контента
    этого достаточно (KISS).
    """

    def __init__(self, source: list[dict]):
        self._words: list[Word] = [Word.from_dict(row) for row in source]
        self._by_id: dict[int, Word] = {w.id: w for w in self._words}

    async def get_all(self) -> list[Word]:
        return list(self._words)

    async def get_by_id(self, word_id: int) -> Word | None:
        return self._by_id.get(word_id)

    async def get_random(self, count: int) -> list[Word]:
        return random.sample(self._words, min(count, len(self._words)))
