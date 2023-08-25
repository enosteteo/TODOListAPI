from app.tasks.models import Task
from app.extensions import db


class TaskService():
    def create_task(self, title, description, user_id, status='TODO'):
        task: Task = Task(title, description, status, user_id)
        db.session.add(task)
        db.session.commit()
        return task.to_dict()
    
    def get_task(self, task_id, user_id):
        task = Task.query.filter_by(user_id=user_id, id=task_id).first_or_404()
        return task.to_dict()

    def update_task(self, task_id, status, title, description, user_id):
        task = Task.query.filter_by(user_id=user_id, id=task_id).first_or_404()
        task.title = title
        task.description = description
        task.status = status
        db.session.commit()
        return task.to_dict()
    
    def delete_task(self, task_id, user_id):
        task = Task.query.filter_by(user_id=user_id, id=task_id).first_or_404()
        db.session.delete(task)
        db.session.commit()
        return task.to_dict()

    def get_tasks(self, user_id):
        tasks:list[Task] = Task.query.filter_by(user_id=user_id).all()
        return tasks
