#!/usr/bin/python3
""" that moduel to map the mysql db using sqlalchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ a class to connect to 'states' table"""

    __tablename__ = "states"
    id = Column(
        "id", Integer, nullable=False, autoincrement=True,
        primary_key=True, unique=True
        )
    name = Column("name", String(128), nullable=False)
