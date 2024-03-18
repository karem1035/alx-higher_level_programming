#!/usr/bin/python3
"""
script that lists all State objects from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    # Constructing the connection URL using command-line arguments
    url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # Creating the SQLAlchemy engine with pool pre-ping enabled
    engine = create_engine(url, pool_pre_ping=True)

    # Creating the tables defined in the models
    Base.metadata.create_all(engine)

    # Creating a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Creating a new session
    session = Session()

    # Getting the state with id 2
    state = session.query(State)\
                   .filter(State.id == 2)\
                   .first()

    # Changing the name of the state with id 2
    state.name = "New Mexico"

    # Session Commit
    session.commit()

    # Cleaning the session
    session.close()
