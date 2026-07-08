"""Композиционный корень: единственное место создания конкретных реализаций.

Переход на Google Sheets = заменить строку создания репозитория.
Простая фабрика вместо DI-контейнера — это KISS.
"""
from __future__ import annotations

from dataclasses import dataclass

from config import settings

from data.words_data import WORDS
from data.verbs_data import VERBS
from data.texts_data import TEXTS
from data.sentences_data import SENTENCES

from repositories.pyfile import (
    PyFileWordRepository,
    PyFileVerbRepository,
    PyFileTextRepository,
    PyFileSentenceRepository,
)
from repositories.json_settings_repo import JsonSettingsRepository
from repositories.json_stats_repo import JsonStatsRepository
from repositories.json_srs_repo import JsonSrsRepository
from repositories.json_progress_repo import JsonProgressRepository

from providers.tts import EdgeTTSProvider

from services import (
    QuizService,
    VocabularyService,
    VerbService,
    SentenceService,
    ListeningService,
    SettingsService,
    StatsService,
    SrsService,
    ProgressService,
)


@dataclass
class Container:
    vocabulary: VocabularyService
    verbs: VerbService
    sentences: SentenceService
    listening: ListeningService
    quiz: QuizService
    settings: SettingsService
    stats: StatsService
    srs: SrsService
    progress: ProgressService


def build_container() -> Container:
    # --- источники данных ---  ← здесь меняется .py → Google Sheets
    word_repo = PyFileWordRepository(WORDS)
    verb_repo = PyFileVerbRepository(VERBS)
    text_repo = PyFileTextRepository(TEXTS)
    sentence_repo = PyFileSentenceRepository(SENTENCES)
    settings_repo = JsonSettingsRepository(settings.settings_file)
    stats_repo = JsonStatsRepository(settings.stats_file)
    srs_repo = JsonSrsRepository(settings.srs_file)
    progress_repo = JsonProgressRepository(settings.progress_file)

    # --- провайдеры ---
    tts = EdgeTTSProvider(settings.tts_voice, settings.tts_cache_dir)

    # --- сервисы ---
    return Container(
        vocabulary=VocabularyService(word_repo),
        verbs=VerbService(verb_repo),
        sentences=SentenceService(sentence_repo),
        listening=ListeningService(text_repo, tts),
        quiz=QuizService(),
        settings=SettingsService(settings_repo),
        stats=StatsService(stats_repo),
        srs=SrsService(srs_repo),
        progress=ProgressService(progress_repo),
    )
