#!/usr/bin/python3
"""
a script that prints the State object with the name passed as argument
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

    # Querying all State objects, ordered by id in ascending order
    result = session.query(State).filter(State.name == argv[4]).first()

    # Printing the result
    if result:
        print(result.id)
    else:
        print("Not found")

    # Cleaning the session
    session.close()
