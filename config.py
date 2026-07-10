"""Конфигурация приложения.

Читает .env без сторонних зависимостей (stdlib), секреты в коде не хранятся.
Импортируется как `from config import settings`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


def _resolve_path(path_value: str | os.PathLike[str] | None, default: str) -> Path:
    candidate = Path(path_value or default)
    if candidate.is_absolute():
        return candidate
    return BASE_DIR / candidate


def _load_env(path: str | os.PathLike[str] | None = None) -> None:
    env_path = _resolve_path(path, ".env")
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_env()


class Settings:
    def __init__(self) -> None:
        token = os.environ.get("BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN")
        if not token:
            raise RuntimeError(
                "BOT_TOKEN не задан. Установи переменную окружения BOT_TOKEN или добавь её в Railway/ .env."
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
        self.settings_file = str(_resolve_path(os.environ.get("SETTINGS_FILE"), "settings.json"))
        self.stats_file = str(_resolve_path(os.environ.get("STATS_FILE"), "stats.json"))
        self.srs_file = str(_resolve_path(os.environ.get("SRS_FILE"), "srs.json"))
        self.progress_file = str(_resolve_path(os.environ.get("PROGRESS_FILE"), "progress.json"))

        # Напоминания
        self.reminder_hour = int(os.environ.get("REMINDER_HOUR", "10"))  # час дня (0-23), локальное время
        self.tts_cache_dir = str(_resolve_path(os.environ.get("TTS_CACHE_DIR"), "tts_cache"))


settings = Settings()
