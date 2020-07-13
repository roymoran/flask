"""Module allows to run operations on database"""
from src.app.persistence.db_config import Base

class Schema:
    """Class for running operations on database"""
    def __init__(self):
        pass

    @classmethod
    def create(cls):
        """Create database schema"""
        Base.metadata.create_all()

    @classmethod
    def update(cls):
        """Updatee database schema"""
        Base.metadata.create_all()

    @classmethod
    def drop(cls):
        """Drop database schema and all data"""
        Base.metadata.drop_all()

    def seed(self):
        """Method to seed database with test data"""

    def create_if_not_exist(self):
        """Utility method to create db if does not exists"""

Schema.create()
