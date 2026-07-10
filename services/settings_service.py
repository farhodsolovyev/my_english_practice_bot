from __future__ import annotations

from models import UserSettings
from repositories.base import AbstractSettingsRepository
from settings_catalog import LEVEL_OPTIONS, TIME_OPTIONS, SIZE_OPTIONS, VOICE_OPTIONS

# Допустимые значения по каждому полю (из каталога) — для валидации.
_ALLOWED = {
    "level": [v for v, _ in LEVEL_OPTIONS],
    "quiz_seconds": [v for v, _ in TIME_OPTIONS],
    "quiz_size": [v for v, _ in SIZE_OPTIONS],
    "voice": [v for v, _ in VOICE_OPTIONS],
}


class SettingsService:
    def __init__(self, repo: AbstractSettingsRepository):
        self._repo = repo

    async def get(self, user_id: int) -> UserSettings:
        return await self._repo.get(user_id)

    async def update(self, user_id: int, field: str, value) -> UserSettings:
        if field not in _ALLOWED or value not in _ALLOWED[field]:
            raise ValueError(f"Недопустимая настройка {field}={value!r}")
        s = await self._repo.get(user_id)
        setattr(s, field, value)
        await self._repo.save(s)
        return s
