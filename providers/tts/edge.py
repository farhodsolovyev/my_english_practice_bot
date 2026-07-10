from __future__ import annotations

import hashlib
from pathlib import Path

import edge_tts

from providers.tts.base import AbstractTTSProvider, Speed


class EdgeTTSProvider(AbstractTTSProvider):
    """TTS на edge-tts с файловым кэшем. Ключ кэша — хэш от (голос, скорость, текст)."""

    _RATE = {Speed.SLOW: "-25%", Speed.NORMAL: "+0%", Speed.FAST: "+30%"}

    def __init__(self, default_voice: str, cache_dir: str):
        self._default_voice = default_voice
        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, text: str, speed: Speed, voice: str) -> Path:
        key = f"{voice}|{speed.value}|{text}"
        digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]
        return self._cache_dir / f"{digest}.mp3"

    async def synthesize(self, text: str, speed: Speed = Speed.NORMAL, voice: str | None = None) -> str:
        voice = voice or self._default_voice
        path = self._cache_path(text, speed, voice)
        if path.exists():
            return str(path)

        communicate = edge_tts.Communicate(text, voice, rate=self._RATE[speed])
        await communicate.save(str(path))
        return str(path)
