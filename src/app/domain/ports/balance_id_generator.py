from typing import Protocol
from uuid import UUID


class BalanceIdGenerator(Protocol):

    def generate(self) -> UUID: ...