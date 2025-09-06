from app.domain.enums.currency import Currencies
s
from app.domain.exceptions.base import DomainError


def validate_payment_currency_is_allowed(payment_currency_value: Currencies):
    if payment_currency_value not in Currencies:
        raise DomainError(f'Payment currency {payment_currency_value} is not allowed')