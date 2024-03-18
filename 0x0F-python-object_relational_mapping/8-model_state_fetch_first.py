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

    # Querying the first State objects
    result = session.query(State).order_by(State.id.asc()).first()

    # Printing the results
    if result:
        print(f"{result.id}: {result.name}")
    else:
        print("Nothing")

    # Cleaning the session
    session.close()
