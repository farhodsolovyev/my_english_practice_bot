from __future__ import annotations

import json
import asyncio
from pathlib import Path

from repositories.base import AbstractSrsRepository


class JsonSrsRepository(AbstractSrsRepository):
    """Интервальное повторение: {user_id: {word_id: {"box": n, "due": day}}}."""

    def __init__(self, file_path: str):
        self._path = Path(file_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()
        self._cache: dict = self._load()

    def _load(self) -> dict:
        if not self._path.exists():
            return {}
        return json.loads(self._path.read_text(encoding="utf-8"))

    def _flush(self) -> None:
        self._path.write_text(json.dumps(self._cache, ensure_ascii=False), encoding="utf-8")

    async def get(self, user_id: int, word_id: int) -> tuple[int, int]:
        e = self._cache.get(str(user_id), {}).get(str(word_id))
        return (e["box"], e["due"]) if e else (0, 0)

    async def set(self, user_id: int, word_id: int, box: int, due_day: int) -> None:
        async with self._lock:
            self._cache.setdefault(str(user_id), {})[str(word_id)] = {"box": box, "due": due_day}
            self._flush()

    async def due(self, user_id: int, today: int) -> list[int]:
        user = self._cache.get(str(user_id), {})
        return [int(wid) for wid, e in user.items() if e["due"] <= today]

    async def boxes(self, user_id: int) -> list[int]:
        return [e["box"] for e in self._cache.get(str(user_id), {}).values()]

    async def users(self) -> list[int]:
        return [int(uid) for uid in self._cache]
