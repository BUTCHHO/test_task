from typing import Protocol

from app.domain.value_objects.user.raw_password import RawUserPassword
from app.domain.value_objects.user.password_hash import UserPasswordHash

class UserPasswordHasher(Protocol):

    def hash(self, raw_password: RawUserPassword) -> bytes: ...

    def verify(self, raw_password: RawUserPassword, hash_password: UserPasswordHash) -> bool: ...