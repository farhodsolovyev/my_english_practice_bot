from dataclasses import dataclass


@dataclass(frozen=True)
class IrregularVerb:
    id: int
    v1: str           # Present (infinitive)
    v2: str           # Past Simple
    v3: str           # Past Participle
    translation: str

    @classmethod
    def from_dict(cls, data: dict) -> "IrregularVerb":
        return cls(
            id=data["id"],
            v1=data["v1"],
            v2=data["v2"],
            v3=data["v3"],
            translation=data["translation"],
        )
