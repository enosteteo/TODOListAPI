import uuid

from app.tasks.models import Task

class UserTO:
    id:uuid.UUID
    name:str
    username:str
    tasks:Task

    def __init__(self, id, name, username, tasks=None):
        self.id = id
        self.name = name
        self.username = username
        self.tasks = tasks
    
    def __repr__(self):
        return f"<UserTO {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "tasks": self.tasks
        }

    def from_dict(self, data):
        for field in ["id", "name", "username", "tasks"]:
            if field in data:
                setattr(self, field, data[field])
