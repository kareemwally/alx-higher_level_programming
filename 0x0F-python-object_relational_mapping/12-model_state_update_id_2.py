#!/usr/bin/python3
"""a module to list all states """

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sys
from model_state import Base, State


def main():
    """ the main function"""
    connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        connect.format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    # Fetch the state with id 2 from the database
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If a state with id 2 is found, update its name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
