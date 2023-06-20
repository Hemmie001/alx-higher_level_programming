#!/usr/bin/python3
"""
This script prints the first State object from the database
hbtn_0e_6_usa
It take 3 arguments: mysql username, mysql password and database name
It uses the module SQLAlchemy
It imports State and Base from model_state - from model_state import Base, State
It script connects to a MySQL server running on localhost at port 3306
The state it displays is the first in states.id
It does not fetch all states from the database before displaying the result
The result is displayed as they are in the example below
If the table states is empty,it prints Nothing followed by a new line
Your code should not be executed when imported
"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Connecting"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    session.close()
