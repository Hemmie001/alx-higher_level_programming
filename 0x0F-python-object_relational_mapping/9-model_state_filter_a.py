#!/usr/bin/python3
"""
This script  lists all State objects that contain the letter a
from the database hbtn_0e_6_usa

It take 3 arguments: mysql username, mysql password and database name
it uses the module SQLAlchemy
It imports State and Base from model_state - 
from model_state import Base, State
it connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results is displayed as they are in the example below
The code should not be executed when imported
"""
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
    first_state = session.query(State).filter(State.name.like('%a%'))
    for sts in first_state:
        print("{}: {}".format(sts.id, sts.name))
    session.close()
