#!/usr/bin/python3
"""
This script primts State objects with name passed as argument from
the database hbtn_0e_6_usa

It take 4 arguments: mysql username, mysql password and database name
it uses the module SQLAlchemy
state name to search (SQL injection free)
It imports State and Base from model_state - 
from model_state import Base, State
it connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
If no state has the name you searched for, display Not found
The code should not be executed when imported
a"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    id_state = session.query(State).filter(State.name.like(
        '%s' % (sys.argv[4], ))).first()
    if id_state is None:
        print("Not found")
    else:
        print(id_state.id)
    session.close()
