from __future__ import annotations

import json
import asyncio
from pathlib import Path

from repositories.base import AbstractStatsRepository


class JsonStatsRepository(AbstractStatsRepository):
    """Точность по уровням: {user_id: {level: {"c": correct, "t": total}}}."""

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
        self._path.write_text(json.dumps(self._cache, ensure_ascii=False, indent=2), encoding="utf-8")

    async def get(self, user_id: int, level: str) -> tuple[int, int]:
        e = self._cache.get(str(user_id), {}).get(level, {})
        return e.get("c", 0), e.get("t", 0)

    async def add(self, user_id: int, level: str, correct: int, total: int) -> None:
        async with self._lock:
            e = self._cache.setdefault(str(user_id), {}).setdefault(level, {"c": 0, "t": 0})
            e["c"] += correct
            e["t"] += total
            self._flush()

    async def reset(self, user_id: int, level: str) -> None:
        async with self._lock:
            self._cache.get(str(user_id), {}).pop(level, None)
            self._flush()
