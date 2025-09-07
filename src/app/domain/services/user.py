from app.domain.ports.user_id_generator import UserIDGenerator
from app.domain.ports.user_password_hasher import UserPasswordHasher

from app.domain.entities.user import User
from app.domain.value_objects.user.user_name.user_name import UserName
from app.domain.value_objects.user.user_id import UserID
from app.domain.value_objects.user.raw_password import RawUserPassword
from app.domain.value_objects.user.password_hash import UserPasswordHash
from app.domain.enums.user.roles import UserRoles


class UserService:

    def __init__(self, user_password_hasher: UserPasswordHasher, user_id_generator: UserIDGenerator):
        self._user_password_hasher = user_password_hasher
        self._user_id_generator = user_id_generator

    def create_user(self, username: UserName, raw_password: RawUserPassword, role: UserRoles) -> User:
        password_hash = UserPasswordHash(self._user_password_hasher.hash(raw_password))
        user_id = UserID(self._user_id_generator.generate())
        return User(id=user_id,
                    name=username,
                    password_hash=password_hash,
                    role=role,
                    is_active=True,)

    def toggle_user_admin(self, user: User, is_admin: bool):
        if is_admin:
            user.role = UserRoles.ADMIN
            return
        user.role = UserRoles.USER

    def toggle_user_activation(self, user: User, is_active: bool):
        user.is_active = is_active

    def change_password(self, user: User, new_raw_password: RawUserPassword):
        new_password_hash = UserPasswordHash(self._user_password_hasher.hash(new_password))
        user.password_hash = new_password_hash

    def change_username(self, user: User, new_username: UserName):
        user.username = new_username

    def verify_password(self, user: User, raw_password: RawUserPassword):
        self._user_password_hasher.verify(raw_password, user.password_hash)