#!/usr/bin/python3
from model_state import Base, State
from sys import argv
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = sa.create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for i in query:
        print(i.name)
