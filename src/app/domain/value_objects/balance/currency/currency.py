from dataclasses import dataclass

from app.domain.value_objects.base import ValueObject
from app.domain.enums.currency import Currencies

from app.domain.value_objects.balance.currency.validation import validate_currency_is_allowed

@dataclass
class BalanceCurrency(ValueObject):
    value: Currencies

    def __post_init__(self):
        validate_currency_is_allowed(self.value)
        super().__post_init__()