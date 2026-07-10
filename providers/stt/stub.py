from providers.stt.base import AbstractSTTProvider, STTResult


class StubSTTProvider(AbstractSTTProvider):
    """Заглушка: фиксирует интерфейс, реальный движок подключим в этапе Speaking."""

    async def transcribe(self, audio_path: str) -> STTResult:
        raise NotImplementedError("STT провайдер ещё не реализован")
