"""Конфигурация приложения.

Читает .env без сторонних зависимостей (stdlib), секреты в коде не хранятся.
Импортируется как `from config import settings`.
"""
from __future__ import annotations

import os
from pathlib import Path


def _load_env(path: str = ".env") -> None:
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_env()


class Settings:
    def __init__(self) -> None:
        token = os.environ.get("BOT_TOKEN")
        if not token:
            raise RuntimeError(
                "BOT_TOKEN не задан. Скопируй .env.example в .env и впиши токен от @BotFather."
            )
        self.bot_token = token

        # TTS
        self.tts_voice = os.environ.get("TTS_VOICE", "en-US-AriaNeural")
        self.tts_voice_male = os.environ.get("TTS_VOICE_MALE", "en-US-GuyNeural")

        # Quiz
        self.quiz_options = int(os.environ.get("QUIZ_OPTIONS", "4"))
        self.quiz_size = int(os.environ.get("QUIZ_SIZE", "10"))
        self.quiz_deadline_seconds = int(os.environ.get("QUIZ_DEADLINE_SECONDS", "15"))

        # Storage
        self.settings_file = os.environ.get("SETTINGS_FILE", "settings.json")
        self.stats_file = os.environ.get("STATS_FILE", "stats.json")
        self.srs_file = os.environ.get("SRS_FILE", "srs.json")
        self.progress_file = os.environ.get("PROGRESS_FILE", "progress.json")

        # Напоминания
        self.reminder_hour = int(os.environ.get("REMINDER_HOUR", "10"))  # час дня (0-23), локальное время
        self.tts_cache_dir = os.environ.get("TTS_CACHE_DIR", "tts_cache")


settings = Settings()
