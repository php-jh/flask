from flask import current_app
from orator import DatabaseManager


class Database:

    @staticmethod
    def db():
        return DatabaseManager(current_app.config['ORATOR_DATABASES'])
