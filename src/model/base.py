from src.config.database import Database


class Base:
    db = None

    def __init__(self):
        self.db = Database.db()
