from users.model import User
from users.server import UserServer
from users.user_to import UserTO

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

from . import router

server = UserServer()

@users_blueprint.route("/", methods=['GET', 'POST'])
def hello_users():
  if request.method == 'GET':
    users: list[UserTO] = server.get_users()
    return ''.join([f'<p>ID: {user.id} | Name: {user.name} | Username: {user.username}</p>\n' for user in users])
  elif request.method == 'POST':
    print(f'{request.get_json()}')
    request_data = request.get_json()
    user_created: UserTO = server.create_user(User(request_data['name'], request_data['username'], request_data['password']))  
    return f'User: {user_created.username} was created. The total number of users is {len(server.get_users())}. The user uuid is {user_created.id}'
