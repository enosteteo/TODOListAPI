import uuid

from users.model import User
from users.user_to import UserTO

users: list[User] = []


class UserServer:
    def create_user(self, user: User) -> UserTO:
        users.append(user)
        return UserTO(user.id, user.name, user.username)

    def get_user(self, user_id: uuid.UUID):
        pass

    def get_users(self) -> list[UserTO]:
        return [UserTO(user.id, user.name, user.username) for user in users]

    def update_user(self, user_id: uuid.UUID, user: User):
        pass

    def delete_user(self, user_id: uuid.UUID):
        pass

    def get_user_by_username(self, username: str):
        pass
