from app.extensions import db
from app.tasks.models import Task
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    tasks = db.relationship(Task, backref="user", lazy='select', )

    def __repr__(self):
        return f"<User {self.username}>"

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "tasks": [task.to_dict() for task in self.tasks] if self.tasks != [] else []
        }

    def from_dict(self, data):
        for field in ["name", "username", "password"]:
            if field in data:
                setattr(self, field, data[field])
