#!/usr/bin/python3
"""
This script that prints the first State object from the database
hbtn_0e_6_usa
Take 3 arguments: mysql username, mysql password and database name
Uses the module SQLAlchemy
Imports State and Base from model_state - from model_state import Base, State
Cconnect to a MySQL server running on localhost at port 3306
Changes the name of the State where id = 2 to New Mexico
The code is not executed when imported
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
    estado = session.query(State).get(2)
    estado.name = "New Mexico"
    session.commit()
    session.close()
