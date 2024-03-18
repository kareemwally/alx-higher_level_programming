#!/usr/bin/python3
""" a python module to create cities table"""
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import ForeignKey


class City(Base):
    """ a class for cities table"""
    __tablename__ = "cities"
    id = Column(
        "id", Integer, nullable=False, autoincrement=True,
        primary_key=True, unique=True
        )
    name = Column("name", String(128), nullable=False)
    state_id = Column(ForeignKey("State.id"))
