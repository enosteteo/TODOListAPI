from flask import request, url_for, redirect
from app.users import bp

from app.users.models import User
from app.users.service import UserService
from app.users.user_to import UserTO


service = UserService()

@bp.route("/", methods=["GET"])
def index():
    users = service.get_all_users()
    return ''.join([f'<p>ID: {user.id} | Name: {user.name} | Username: {user.username} | Tasks: {user.tasks}</p>\n' for user in users])


@bp.route("/first")
def get_first():
    user = User.query.first()
    return f"teste: {user}"