import uuid


class HR:
    next_id = uuid.uuid4()

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

