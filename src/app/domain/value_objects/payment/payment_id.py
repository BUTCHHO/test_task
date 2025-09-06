from dataclasses import dataclass

from uuid import UUID

from app.domain.value_objects.base import ValueObject


@dataclass
class PaymentID(ValueObject):
    value: UUID

    def __post_init__(self):
        super().__post_init__()