from dataclasses import dataclass

from app.domain.entities.base import Entity
from app.domain.value_objects.balance.balance_id import BalanceID

from app.domain.value_objects.payment.payment_id import PaymentID
from app.domain.value_objects.payment.payment_currency.payment_currency import PaymentCurrency
from app.domain.value_objects.payment.payment_date import PaymentDate
from app.domain.value_objects.payment.payment_amount import PaymentAmount
from app.domain.enums.payment import PaymentStatuses


@dataclass
class Payment(Entity):
    id: PaymentID
    amount: PaymentAmount
    currency: PaymentCurrency
    date: PaymentDate
    status: PaymentStatuses

    receiver_balance_id: BalanceID