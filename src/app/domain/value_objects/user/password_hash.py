from dataclasses import dataclass

from app.domain.value_objects.base import ValueObject


class UserPasswordHash(ValueObject):
    value: bytes
    def __post_init__(self):
        super().__post_init__()