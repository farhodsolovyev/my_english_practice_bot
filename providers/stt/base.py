"""Абстракция распознавания речи (для раздела Speaking). Реализация — позже."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class STTResult:
    text: str
    confidence: float = 0.0


class AbstractSTTProvider(ABC):
    @abstractmethod
    async def transcribe(self, audio_path: str) -> STTResult:
        """Распознаёт речь из аудиофайла в текст."""
        ...
