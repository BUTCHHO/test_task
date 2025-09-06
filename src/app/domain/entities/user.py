from dataclasses import dataclass

from app.domain.entities.base import Entity
from app.domain.value_objects.user.user_id import UserID
from app.domain.value_objects.user.user_name.user_name import UserName
from app.domain.value_objects.user.password_hash import UserPasswordHash
from app.domain.enums.user.roles import UserRoles

@dataclass
class User(Entity):
    id: UserID
    name: UserName
    password_hash: UserPasswordHash
    role: UserRoles