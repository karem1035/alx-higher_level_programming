#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class State(Base):
    __tablename__ = "user_account",
    id = Column(Integer,  nullable=False, autoincrement=True, primary_key=True),
    name = Column(String(128), nullable=False)
