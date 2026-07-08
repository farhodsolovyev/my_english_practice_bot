"""Services module."""


class QuizService:
    pass


class VocabularyService:
    def __init__(self, repo):
        self.repo = repo


class VerbService:
    def __init__(self, repo):
        self.repo = repo


class SentenceService:
    def __init__(self, repo):
        self.repo = repo


class ListeningService:
    def __init__(self, repo, tts):
        self.repo = repo
        self.tts = tts


class SettingsService:
    def __init__(self, repo):
        self.repo = repo


class StatsService:
    def __init__(self, repo):
        self.repo = repo


class SrsService:
    def __init__(self, repo):
        self.repo = repo


class ProgressService:
    def __init__(self, repo):
        self.repo = repo

