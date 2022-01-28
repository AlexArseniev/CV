import uuid


class User:
    user_id = uuid.uuid4()

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __str__(self):
        return f'| {self.user_id:20.20} | {self.name:10.10} |\n'

