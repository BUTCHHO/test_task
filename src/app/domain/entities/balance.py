from dataclasses import dataclass

from app.domain.entities.base import Entity

from app.domain.value_objects.balance.balance_id import BalanceID
from app.domain.value_objects.balance.count.count import BalanceCount
from app.domain.value_objects.user.user_id import UserID
from app.domain.value_objects.balance.currency.currency import BalanceCurrency

@dataclass
class Balance(Entity):
    id: BalanceID
    count: BalanceCount
    user_id: UserID
    currency: BalanceCurrency
    is_frozen: bool