#!/usr/bin/python3
"""a module to list all states """


def main():
    """ the main function"""
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    import sys
    from model_state import Base, State
    connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
        connect.format(sys.argv[1], sys.argv[2], sys.argv[3])
        )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    new_item = State(name="Louisiana")
    session.add(new_item)
    session.commit()

    print("{}".format(new_item.id))

    session.close()


if __name__ == "__main__":
    main()
