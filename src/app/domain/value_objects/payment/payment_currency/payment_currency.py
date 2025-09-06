from dataclasses import dataclass

from app.domain.value_objects.base import ValueObject
from app.domain.value_objects.payment.payment_currency.validation import validate_payment_currency_is_allowed

from app.domain.enums.currency import Currencies

@dataclass
class PaymentCurrency(ValueObject):
    value: Currencies

    def __post_init__(self):
        validate_payment_currency_is_allowed(self.value)
        super().__post_init__()