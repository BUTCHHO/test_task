from typing import Protocol

from uuid import UUID

class UserIDGenerator(Protocol):

    def generate(self) -> UUID: ...

