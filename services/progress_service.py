from __future__ import annotations

import datetime

from repositories.base import AbstractProgressRepository

DAILY_GOAL = 20  # ответов в день — цель


class ProgressService:
    """Серия дней (streak) и дневная активность. Любой ответ считается практикой."""

    def __init__(self, repo: AbstractProgressRepository):
        self._repo = repo

    @staticmethod
    def _today() -> int:
        return datetime.date.today().toordinal()

    async def record(self, user_id: int) -> None:
        p = await self._repo.get(user_id)
        today = self._today()
        if p.day == today:
            p.today += 1
        elif p.day == today - 1:      # занимался вчера → серия продолжается
            p.streak += 1
            p.today = 1
            p.day = today
        else:                          # первый раз или пропуск дня → серия с нуля
            p.streak = 1
            p.today = 1
            p.day = today
        p.best = max(p.best, p.streak)
        p.total += 1
        await self._repo.save(p)

    async def summary(self, user_id: int) -> dict:
        p = await self._repo.get(user_id)
        today = self._today()
        # серия жива, если последний активный день сегодня или вчера
        streak = p.streak if p.day >= today - 1 else 0
        today_count = p.today if p.day == today else 0
        return {
            "streak": streak, "best": p.best, "total": p.total,
            "today": today_count, "goal": DAILY_GOAL,
        }
