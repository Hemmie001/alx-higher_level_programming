#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password and database name
it uses the module SQLAlchemy
It imports State and Base from model_state - from model_state import Base, State
It connects to a MySQL server running on localhost at port 3306
It Prints the new states.id after creation
Your code should not be executed when imported
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
    estado = State()
    estado.name = 'Louisiana'
    session.add(estado)
    session.commit()
    print(estado.id)
    session.close()
