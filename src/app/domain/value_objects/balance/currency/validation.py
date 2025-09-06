

from app.domain.enums.currency import Currencies

from app.domain.value_objects.balance.currency.constants import ALLOWED_BALANCE_CURRENCIES

from app.domain.exceptions.base import DomainError


def validate_currency_is_allowed(currency_value: Currencies):
    if currency_value not in ALLOWED_BALANCE_CURRENCIES:
        raise DomainError(f"Currency '{currency_value}' is not allowed")