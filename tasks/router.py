from . import tasks_blueprint

@tasks_blueprint.route("/", methods=['GET'])
def hello_tasks():
  return 'hello tasks'