"""Единый движок теста для любого раздела (слова, глаголы, предложения).

Разделы поставляют список QuizItem (вопрос + правильный ответ), а сборка
вариантов/перемешивание/индекс правильного — здесь. Сервис без состояния.
"""
from __future__ import annotations

import random
from dataclasses import dataclass

from models import QuizQuestion


@dataclass(frozen=True)
class QuizItem:
    prompt: str          # HTML-текст вопроса
    answer: str          # правильный ответ (текст кнопки)
    note: str | None = None  # показывается после ответа (напр. перевод предложения)
    answer_translation: str | None = None  # перевод слова-ответа (для показа вариантов)
    ref: int | None = None   # id сущности (напр. слова) — для SRS


class QuizService:
    def build(self, items: list[QuizItem], size: int, n_options: int,
              ask_from: list[QuizItem] | None = None) -> list[QuizQuestion]:
        """Собирает вопросы теста.

        items    — общий пул (из него берутся дистракторы и переводы).
        ask_from — из чего задавать вопросы (по умолчанию = items). Для повторения
                   сюда передаётся подмножество слов «к сроку», а дистракторы всё равно
                   берутся из всего пула.
        """
        if len(items) < 2:
            return []

        # карта ответ → перевод (если разделы её дают, напр. предложения/глаголы)
        translations = {i.answer: i.answer_translation for i in items if i.answer_translation}

        candidates = ask_from if ask_from is not None else items
        if not candidates:
            return []
        chosen = random.sample(candidates, min(size, len(candidates)))
        questions: list[QuizQuestion] = []
        for item in chosen:
            # пул дистракторов — уникальные чужие ответы
            pool = list({i.answer for i in items if i.answer != item.answer})
            random.shuffle(pool)
            options = pool[: max(0, n_options - 1)] + [item.answer]
            random.shuffle(options)
            option_notes = [translations.get(opt) for opt in options] if translations else None
            if option_notes and not any(option_notes):
                option_notes = None
            questions.append(QuizQuestion(
                prompt=item.prompt,
                options=options,
                correct=options.index(item.answer),
                note=item.note,
                option_notes=option_notes,
                ref=item.ref,
            ))
        return questions
