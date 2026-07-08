"""Text-to-speech provider."""


class EdgeTTSProvider:
    def __init__(self, voice, cache_dir):
        self.voice = voice
        self.cache_dir = cache_dir

