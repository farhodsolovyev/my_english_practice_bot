from __future__ import annotations

import datetime

from repositories.base import AbstractSrsRepository

# Коробки Лейтнера: box → через сколько дней слово снова к повторению (верный ответ).
_INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
_MAX_BOX = 5
_LEARNED_BOX = 4  # с этой коробки слово считаем «выученным»


class SrsService:
    """Интервальное повторение слов. Верный ответ двигает слово в коробку выше
    (интервал растёт), ошибка возвращает в первую и показывает слово снова сегодня."""

    def __init__(self, repo: AbstractSrsRepository):
        self._repo = repo

    @staticmethod
    def _today() -> int:
        return datetime.date.today().toordinal()

    async def review(self, user_id: int, word_id: int, correct: bool) -> None:
        box, _ = await self._repo.get(user_id, word_id)
        today = self._today()
        if correct:
            box = min(_MAX_BOX, box + 1)
            due = today + _INTERVALS[box]
        else:
            box = 1
            due = today  # ошибся — вернуть к повторению сегодня
        await self._repo.set(user_id, word_id, box, due)

    async def due_ids(self, user_id: int) -> list[int]:
        return await self._repo.due(user_id, self._today())

    async def progress(self, user_id: int) -> dict:
        boxes = await self._repo.boxes(user_id)
        return {
            "total": len(boxes),
            "learned": sum(1 for b in boxes if b >= _LEARNED_BOX),
            "due": len(await self.due_ids(user_id)),
        }

    async def users_with_due(self) -> list[int]:
        today = self._today()
        result = []
        for uid in await self._repo.users():
            if await self._repo.due(uid, today):
                result.append(uid)
        return result
