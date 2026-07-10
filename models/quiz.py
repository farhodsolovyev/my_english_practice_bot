"""Модель сессии теста + чистая логика (без Telegram).

Раньше это жило сырыми dict внутри хендлера quiz_flow. Теперь состояние
типизировано, а решения (что верно, когда следующий, сколько процентов)
инкапсулированы в методах — хендлер занимается только I/O.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QuizQuestion:
    prompt: str            # HTML-текст вопроса
    options: list[str]     # варианты ответа
    correct: int           # индекс правильного
    note: str | None = None  # показывается после ответа (напр. перевод предложения)
    # перевод каждого варианта (для reveal), выровнен с options; None где нет
    option_notes: list | None = None
    ref: int | None = None   # id сущности (напр. слова) — для SRS; None где неприменимо

    def to_dict(self) -> dict:
        return {
            "prompt": self.prompt, "options": self.options, "correct": self.correct,
            "note": self.note, "option_notes": self.option_notes, "ref": self.ref,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "QuizQuestion":
        return cls(
            prompt=d["prompt"], options=d["options"], correct=d["correct"],
            note=d.get("note"), option_notes=d.get("option_notes"), ref=d.get("ref"),
        )


@dataclass
class QuizSession:
    section: str           # vocabulary | verbs | sentences
    user_id: int
    chat_id: int
    questions: list[QuizQuestion]
    level: str | None = None   # для адаптива сложности (тест слов)
    deadline: int = 15         # сек на ответ, 0 → без таймера
    i: int = 0                 # индекс текущего вопроса
    qid: int = 0               # id вопроса — защита от гонок таймера
    correct: int = 0
    wrong: int = 0
    msg_id: int | None = None  # id сообщения текущего вопроса

    # ── чистая логика ──
    @property
    def total(self) -> int:
        return len(self.questions)

    @property
    def current(self) -> QuizQuestion:
        return self.questions[self.i]

    @property
    def is_finished(self) -> bool:
        return self.i >= self.total

    @property
    def percent(self) -> int:
        answered = self.correct + self.wrong
        return round(self.correct / answered * 100) if answered else 0

    def check(self, chosen: int | None) -> bool:
        return chosen is not None and chosen == self.current.correct

    def register(self, is_correct: bool) -> None:
        if is_correct:
            self.correct += 1
        else:
            self.wrong += 1

    def advance(self) -> None:
        """К следующему вопросу; смена qid инвалидирует таймер прошлого."""
        self.i += 1
        self.qid += 1

    # ── (де)сериализация для FSM ──
    def to_dict(self) -> dict:
        return {
            "section": self.section, "user_id": self.user_id, "chat_id": self.chat_id,
            "questions": [q.to_dict() for q in self.questions], "level": self.level,
            "deadline": self.deadline, "i": self.i, "qid": self.qid,
            "correct": self.correct, "wrong": self.wrong, "msg_id": self.msg_id,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "QuizSession":
        return cls(
            section=d["section"], user_id=d["user_id"], chat_id=d["chat_id"],
            questions=[QuizQuestion.from_dict(q) for q in d["questions"]],
            level=d.get("level"), deadline=d.get("deadline", 15),
            i=d.get("i", 0), qid=d.get("qid", 0),
            correct=d.get("correct", 0), wrong=d.get("wrong", 0), msg_id=d.get("msg_id"),
        )
