from providers.ai.base import AbstractAIProvider


class StubAIProvider(AbstractAIProvider):
    """Заглушка: фиксирует интерфейс до подключения реальной модели."""

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError("AI провайдер ещё не реализован")
