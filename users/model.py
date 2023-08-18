import uuid

class User:
    id:uuid.UUID
    name:str
    username:str
    password:str

    def __init__(self, name, username, password):
        self.id = uuid.uuid4()
        self.name = name
        self.username = username
        self.password = password


    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password
        }

    def from_dict(self, data):
        for field in ["name", "username", "password"]:
            if field in data:
                setattr(self, field, data[field])
