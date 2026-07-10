"""Абстрактные репозитории (DAO).

Сервисы зависят ТОЛЬКО от этих интерфейсов. Добавление нового источника
(Google Sheets) = новый класс-реализация, без правок в services/handlers.
Методы async — чтобы сетевой GoogleSheetsRepository вписался без изменений выше.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from models import Word, IrregularVerb, ListeningText, Sentence, UserSettings, UserProgress


class AbstractWordRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Word]: ...

    @abstractmethod
    async def get_by_id(self, word_id: int) -> Word | None: ...

    @abstractmethod
    async def get_random(self, count: int) -> list[Word]: ...


class AbstractVerbRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[IrregularVerb]: ...

    @abstractmethod
    async def get_by_id(self, verb_id: int) -> IrregularVerb | None: ...

    @abstractmethod
    async def get_random(self, count: int) -> list[IrregularVerb]: ...


class AbstractTextRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[ListeningText]: ...

    @abstractmethod
    async def get_by_id(self, text_id: int) -> ListeningText | None: ...


class AbstractSentenceRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Sentence]: ...


class AbstractSettingsRepository(ABC):
    """Read-write: персональные настройки пользователя."""

    @abstractmethod
    async def get(self, user_id: int) -> UserSettings: ...

    @abstractmethod
    async def save(self, settings: UserSettings) -> None: ...


class AbstractStatsRepository(ABC):
    """Read-write: накопленная точность по уровням (correct, total) для адаптива."""

    @abstractmethod
    async def get(self, user_id: int, level: str) -> tuple[int, int]: ...

    @abstractmethod
    async def add(self, user_id: int, level: str, correct: int, total: int) -> None: ...

    @abstractmethod
    async def reset(self, user_id: int, level: str) -> None: ...


class AbstractProgressRepository(ABC):
    """Read-write: ежедневная активность (серия/цель)."""

    @abstractmethod
    async def get(self, user_id: int) -> UserProgress: ...

    @abstractmethod
    async def save(self, progress: UserProgress) -> None: ...


class AbstractSrsRepository(ABC):
    """Read-write: интервальное повторение — коробка и срок по слову."""

    @abstractmethod
    async def get(self, user_id: int, word_id: int) -> tuple[int, int]:
        """(box, due_day). Для незнакомого слова — (0, 0)."""
        ...

    @abstractmethod
    async def set(self, user_id: int, word_id: int, box: int, due_day: int) -> None: ...

    @abstractmethod
    async def due(self, user_id: int, today: int) -> list[int]:
        """id слов, у которых подошёл срок (due_day <= today)."""
        ...

    @abstractmethod
    async def boxes(self, user_id: int) -> list[int]:
        """Номера коробок всех слов пользователя (для статистики)."""
        ...

    @abstractmethod
    async def users(self) -> list[int]:
        """Все пользователи с записями SRS (для напоминаний)."""
        ...
