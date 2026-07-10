from __future__ import annotations

import json
import asyncio
from pathlib import Path

from models import UserSettings
from repositories.base import AbstractSettingsRepository


class JsonSettingsRepository(AbstractSettingsRepository):
    """Настройки пользователей в одном JSON-файле {user_id: settings}."""

    def __init__(self, file_path: str):
        self._path = Path(file_path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()
        self._cache: dict[int, UserSettings] = self._load()

    def _load(self) -> dict[int, UserSettings]:
        if not self._path.exists():
            return {}
        raw = json.loads(self._path.read_text(encoding="utf-8"))
        return {int(uid): UserSettings.from_dict(s) for uid, s in raw.items()}

    def _flush(self) -> None:
        data = {str(uid): s.to_dict() for uid, s in self._cache.items()}
        self._path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    async def get(self, user_id: int) -> UserSettings:
        s = self._cache.get(user_id)
        if s is None:
            s = UserSettings(user_id=user_id)
            self._cache[user_id] = s
        return s

    async def save(self, settings: UserSettings) -> None:
        async with self._lock:
            self._cache[settings.user_id] = settings
            self._flush()
