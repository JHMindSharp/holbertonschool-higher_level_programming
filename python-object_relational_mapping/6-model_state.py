#!/usr/bin/python3
"""
Defines class State and an instance Base using the SQLAlchemy ORM.
State class:
- inherits from Base
- links to MySQL table states
- class attribute id: represents a column of an auto-generated,
unique integer, can't be null and is a primary key
- class attribute name: represents a column of a string with maximum
28 characters and can't be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
