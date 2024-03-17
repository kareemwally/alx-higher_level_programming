#!/usr/bin/python3
"""a module to list all states """

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import delete
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
    res = session.query(State).filter(State.name.like('%a%')).all()
    for r in res:
        session.delete(r)
    # If a state with id 2 is found, update its name
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
