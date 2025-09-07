from app.domain.value_objects.base import ValueObject


class BalanceCount(ValueObject):
    value: float
    #todo add entity of money (curr + amount)
    def __post_init__(self):
        super().__post_init__()