# pylint: disable=too-few-public-methods
"""Module defines objects which maps to workspaces table"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.app.persistence.db_config import Base

class ExampleEntity(Base):
    """Class defines objects which maps to workspaces table"""
    __tablename__ = 'workspaces'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    value = Column(String(255))
    created_on = Column(DateTime(), default=datetime.utcnow())
    updated_on = Column(DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
