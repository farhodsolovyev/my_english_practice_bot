from __future__ import annotations

from repositories.base import AbstractSentenceRepository
from services.quiz_service import QuizItem
from data.sentence_words_data import WORD_TRANSLATIONS


class SentenceService:
    def __init__(self, sentences: AbstractSentenceRepository):
        self._sentences = sentences

    async def quiz_items(self) -> list[QuizItem]:
        items = await self._sentences.get_all()
        result = []
        for s in items:
            filled = s.text.replace("_", f"<b>{s.answer}</b>")
            note = filled
            if s.translation:
                note += f"\n🇷🇺 {s.translation}"
            result.append(
                QuizItem(
                    prompt=f"✍️ Заполни пропуск:\n\n<b>{s.blanked}</b>",
                    answer=s.answer,
                    note=note,
                    answer_translation=WORD_TRANSLATIONS.get(s.answer.lower()),
                )
            )
        return result
