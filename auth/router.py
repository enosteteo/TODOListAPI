from . import auth_blueprint

@auth_blueprint.route("/login", methods=['GET'])
def hello_auth():
  return 'hello auth'