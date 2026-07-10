"""Доменные модели — общий язык всех слоёв."""
from models.level import Level
from models.word import Word, WordMeaning
from models.verb import IrregularVerb
from models.text import ListeningText
from models.sentence import Sentence
from models.settings import UserSettings
from models.quiz import QuizSession, QuizQuestion
from models.listen import ListenState
from models.progress import UserProgress

__all__ = [
    "Level",
    "Word",
    "WordMeaning",
    "IrregularVerb",
    "ListeningText",
    "Sentence",
    "UserSettings",
    "QuizSession",
    "QuizQuestion",
    "ListenState",
    "UserProgress",
]
