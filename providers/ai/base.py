"""Абстракция LLM/AI. Точка расширения: генерация вопросов, проверка речи,
объяснение ошибок. Реализация (Claude и т.п.) — позже."""
from abc import ABC, abstractmethod


class AbstractAIProvider(ABC):
    @abstractmethod
    async def complete(self, prompt: str) -> str:
        """Базовый текстовый запрос к модели."""
        ...
