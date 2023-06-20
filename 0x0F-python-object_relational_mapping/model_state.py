#!/usr/bin/python3
"""
This is a python file that contains the class definition of a State
and an instance Base = declarative_base():

State class:
1 - inherits from Base Tips
2 - links to the MySQL table states
3 - class attribute id that represents a column of an auto-generated,
****unique integer, can’t be null and is a primary key
4 - class attribute name that represents a column of a string
****with maximum 128 characters and can’t be null
You must use the module SQLAlchemy
This script connects to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be imported before
calling Base.metadata.create_all(engine)a python file that contains
the class definition of a State and an instance Base = declarative_base():

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representation of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, )
    name = Column(String(128), nullable=False)
