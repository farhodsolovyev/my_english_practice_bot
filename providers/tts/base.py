"""Абстракция озвучки. Движок (edge-tts, облачный TTS, ...) меняется без правок выше."""
from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class Speed(str, Enum):
    SLOW = "slow"
    NORMAL = "normal"
    FAST = "fast"


class AbstractTTSProvider(ABC):
    @abstractmethod
    async def synthesize(self, text: str, speed: Speed = Speed.NORMAL, voice: str | None = None) -> str:
        """Возвращает путь к аудиофайлу (mp3). voice=None → голос по умолчанию."""
        ...
