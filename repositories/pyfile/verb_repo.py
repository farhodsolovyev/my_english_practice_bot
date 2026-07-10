from __future__ import annotations

import random

from models import IrregularVerb
from repositories.base import AbstractVerbRepository


class PyFileVerbRepository(AbstractVerbRepository):
    def __init__(self, source: list[dict]):
        self._verbs: list[IrregularVerb] = [IrregularVerb.from_dict(row) for row in source]
        self._by_id: dict[int, IrregularVerb] = {v.id: v for v in self._verbs}

    async def get_all(self) -> list[IrregularVerb]:
        return list(self._verbs)

    async def get_by_id(self, verb_id: int) -> IrregularVerb | None:
        return self._by_id.get(verb_id)

    async def get_random(self, count: int) -> list[IrregularVerb]:
        return random.sample(self._verbs, min(count, len(self._verbs)))
