from enum import Enum


class Level(str, Enum):
    """Уровень сложности (CEFR). str-Enum — удобно сериализовать в JSON и сравнивать."""
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

    @property
    def order(self) -> int:
        """Порядковый номер — для повышения/понижения уровня."""
        return list(Level).index(self)

    def shifted(self, delta: int) -> "Level":
        """Сдвиг уровня на delta ступеней с зажимом в границах."""
        levels = list(Level)
        idx = max(0, min(len(levels) - 1, self.order + delta))
        return levels[idx]
