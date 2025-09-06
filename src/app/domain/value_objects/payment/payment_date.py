from dataclasses import dataclass
from app.domain.value_objects.base import ValueObject

from datetime import datetime

@dataclass
class PaymentDate(ValueObject):
    value: datetime

    def __post_init__(self):
        super().__post_init__()
