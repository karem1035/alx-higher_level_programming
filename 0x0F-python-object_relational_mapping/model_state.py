#!/usr/bin/python3

"""
This Python script defines a SQLAlchemy mapped class for a State entity.
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    """"
    Represesnts a state entity in the database.

    Attributes:
        id (int): The primary key of the state, auto-incremented.
        name (str): The name of the state, max length 128 characters.
    """
    __tablename__ = "user_account"

    id = Column(Integer,  nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
