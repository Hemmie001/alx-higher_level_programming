#!/usr/bin/python3
"""
This ai  a Python file similar to model_state.py named 
model_city.py that contains the class definition of a City.

City class:
it inherits from Base (imported from model_state)
it links to the MySQL table cities
its a class attribute id that represents a column 
of an auto-generated, unique integer, can’t be null and 
is a primary key
its aclass attribute name that represents a column of a
string of 128 characters and can’t be null
its a class attribute state_id that represents a column
of an integer, can’t be null and is a foreign key to states.id
You must use the module SQLAlchemy

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, )
    name = Column(String(128), nullable=False)
