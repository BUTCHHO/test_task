from dataclasses import dataclass
from uuid import UUID

from app.domain.value_objects.base import ValueObject


@dataclass
class UserID(ValueObject):
    value: UUID

    def __post_init__(self):
        super().__post_init__()