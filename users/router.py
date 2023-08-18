from users.model import User
from users.server import UserServer
from users.user_to import UserTO
from . import users_blueprint


server = UserServer()

@users_blueprint.route("/", methods=['GET', 'POST'])
def hello_users():
  if request.method == 'GET':
    users: list[UserTO] = server.get_users()
    return '<br>'.join([f'<p>ID: {user.id} | Name: {user.name} | Username: {user.username}</p>' for user in users]).join('</br>')
  elif request.method == 'POST':
    user_created: UserTO = server.create_user(User(request.form['name'], request.form['username'], request.form['password']))  
    return f'User: {user_created.username} was created. The total number of users is {len(server.get_users())}. The user uuid is {user_created.id}'
