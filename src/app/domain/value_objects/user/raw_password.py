from dataclasses import dataclass

from app.domain.value_objects.base import ValueObject


@dataclass
class RawUserPassword(ValueObject):
    value: str

    def __post_init__(self):
        super().__post_init__()
