#!/usr/bin/python3
"""
This script  prints the first State object from the database
hbtn_0e_6_usa
Take 3 arguments: mysql username, mysql password and database name
Uses the module SQLAlchemy
It imports State and Base from model_state - from model_state 
import Base, State
It connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
it does not execut when imported
"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
