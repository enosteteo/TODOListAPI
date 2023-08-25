import uuid

from app.users.models import User
from app.users.user_to import UserTO
from app.extensions import db


class UserService:
    def create_user(self, user: User) -> UserTO:
        db.session.add(user)
        db.session.commit()
        return UserTO(user.id, user.name, user.username)

    def get_user(self, user_id: uuid.UUID):
        pass

    def get_all_users(self) -> list[UserTO]:
        users:list[User] = User.query.all()
        return [UserTO(user.id, user.name, user.username, user.tasks) for user in users]

    def update_user(self, user_id: uuid.UUID, user: User):
        pass

    def delete_user(self, user_id: uuid.UUID):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user

    def get_user_by_username(self, username: str):
        pass

def find_by_any(obj_origin, search_key):
    pass