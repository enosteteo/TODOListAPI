from app.tasks import bp
from app.tasks.service import TaskService
from flask_login import login_required, current_user
from flask import request, jsonify, make_response, session, json

service = TaskService()

@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_id = current_user.id
    match request.method:
        case "GET":
            request.args.get("status", type=str, default="")
            tasks = service.get_tasks(user_id)
            return json.dumps([task.to_dict() for task in tasks])
        case "POST":
            request_data = request.get_json()
            status = request_data['status']
            title = request_data['title']
            description = request_data['description']

            task = service.create_task(title=title, description=description, status=status, user_id=user_id)
            return jsonify(task)

@bp.route("/<int:task_id>", methods=["GET", "PUT", "DELETE"])
@login_required
def task(task_id):
    user_id = current_user.id
    match request.method:
        case "GET":
            task = service.get_task(task_id, user_id)
            return jsonify(task)

        case "PUT":
            request_data = request.get_json()
            status = request_data['status']
            title = request_data['title']
            description = request_data['description']

            task = service.update_task(task_id=task_id, status=status, title=title, description=description, user_id=user_id)
            return jsonify(task)

        case "DELETE":
            task = service.delete_task(task_id, user_id)
            return jsonify(task)
