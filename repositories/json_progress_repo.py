from __future__ import annotations

import json
import asyncio
from pathlib import Path

from models import UserProgress
from repositories.base import AbstractProgressRepository


class JsonProgressRepository(AbstractProgressRepository):
    """Ежедневная активность в JSON: {user_id: {...}}."""

    def __init__(self, file_path: str):
        self._path = Path(file_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()
        self._cache: dict[int, UserProgress] = self._load()

    def _load(self) -> dict[int, UserProgress]:
        if not self._path.exists():
            return {}
        raw = json.loads(self._path.read_text(encoding="utf-8"))
        return {int(uid): UserProgress.from_dict(p) for uid, p in raw.items()}

    def _flush(self) -> None:
        data = {str(uid): p.to_dict() for uid, p in self._cache.items()}
        self._path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    async def get(self, user_id: int) -> UserProgress:
        p = self._cache.get(user_id)
        if p is None:
            p = UserProgress(user_id=user_id)
            self._cache[user_id] = p
        return p

    async def save(self, progress: UserProgress) -> None:
        async with self._lock:
            self._cache[progress.user_id] = progress
            self._flush()
