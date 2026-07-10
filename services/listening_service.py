from __future__ import annotations

from models import ListeningText
from repositories.base import AbstractTextRepository
from providers.tts import AbstractTTSProvider, Speed

_LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1", "C2"]


class ListeningService:
    def __init__(self, texts: AbstractTextRepository, tts: AbstractTTSProvider):
        self._texts = texts
        self._tts = tts

    async def levels(self) -> list[str]:
        """Уровни, для которых есть тексты (в порядке CEFR)."""
        present = {t.level.value for t in await self._texts.get_all()}
        return [lvl for lvl in _LEVEL_ORDER if lvl in present]

    async def by_level(self, level: str) -> list[ListeningText]:
        return [t for t in await self._texts.get_all() if t.level.value == level]

    async def get(self, text_id: int) -> ListeningText | None:
        return await self._texts.get_by_id(text_id)

    async def audio(self, text: ListeningText, speed: Speed, voice: str | None = None) -> str:
        return await self._tts.synthesize(text.content, speed, voice)
