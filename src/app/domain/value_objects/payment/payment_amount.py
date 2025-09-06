from dataclasses import dataclass
from app.domain.value_objects.base import ValueObject

@dataclass
class PaymentAmount(ValueObject):
    value: float

    def __post_init__(self):
        super().__post_init__()