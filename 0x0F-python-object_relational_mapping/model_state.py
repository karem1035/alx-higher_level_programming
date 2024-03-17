#!/usr/bin/python3
""" File contains the class definition of a State and an instance Base """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ Class representing the state in the database """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), unique=True)
