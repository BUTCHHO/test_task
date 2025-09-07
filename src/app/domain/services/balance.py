from app.domain.entities.balance import Balance

from app.domain.value_objects.balance.count.count import BalanceCount
from app.domain.value_objects.balance.balance_id import BalanceID
from app.domain.value_objects.balance.currency.currency import BalanceCurrency

from app.domain.ports.balance_id_generator import BalanceIdGenerator
from app.domain.value_objects.user.user_id import UserID


class BalanceService:
    def __init__(self, balance_id_generator):
        self._balance_id_generator = balance_id_generator



    def create_balance(self, balance_owner_user_id: UserID):
        balance_id = BalanceID(self._balance_id_generator.generate())
        balance_count = BalanceCount()
        return Balance(id=balance_id, count=balance_count, user_id=balance_owner_user_id, is_frozen=False)
