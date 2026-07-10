from __future__ import annotations

from repositories.base import AbstractVerbRepository
from services.quiz_service import QuizItem


class VerbService:
    def __init__(self, verbs: AbstractVerbRepository):
        self._verbs = verbs

    async def quiz_items(self) -> list[QuizItem]:
        verbs = await self._verbs.get_all()
        return [
            QuizItem(
                prompt=f"🔄 <b>{v.v1}</b>  ({v.translation})\n\nВыбери формы V2 / V3:",
                answer=f"{v.v2} / {v.v3}",
                answer_translation=v.translation,
            )
            for v in verbs
        ]
