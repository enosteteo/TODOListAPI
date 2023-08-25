from flask import Blueprint, url_for, request, jsonify, make_response, session
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.users.models import User

from app import db
from app.users.service import UserService
from app.users.user_to import UserTO

bp = Blueprint('auth', __name__)
service = UserService()

@bp.route('/signup', methods=['POST'])
def signup():
    request_data = request.get_json()

    name = request_data['name']
    username = request_data['username']
    password = request_data['password']

    user = User.query.filter_by(username=username)

    for user in user:
        if (user.to_dict()):
            response = make_response(jsonify({'Error': 'User already exists'}), 409)
            response.headers['Content-Type'] = 'application/json'
            response.headers['Accept'] = 'application/json'
            return response
        break

    new_user = User(name=name, username=username, password=generate_password_hash(password, method='scrypt:32768:8:1'))
    service.create_user(new_user)
    response = make_response(jsonify(new_user.to_dict()), 201)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Accept'] = 'application/json'
    return response

@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()

    username = request_data['username']
    password = request_data['password']
    remember = True if request_data['remember'] else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        response = make_response(jsonify({'Error': 'Please check your login details and try again'}), 401)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username
    login_user(user, remember=remember)
    return 'Acessou'


@bp.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return 'Logout'