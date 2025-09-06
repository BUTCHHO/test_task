from enum import Enum


class PaymentStatuses(Enum):
    PENDING = 0
    PAID = 1
    FAILED = 2
    CANCELLED3 = 3
    EXPIRED = 4
