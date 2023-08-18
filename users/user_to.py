import uuid


class UserTO:
    id:uuid.UUID
    name:str
    username:str

    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
    
    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
        }

    def from_dict(self, data):
        for field in ["id", "name", "username"]:
            if field in data:
                setattr(self, field, data[field])
