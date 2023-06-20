#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
it takes 3 arguments:
1 - mysql username,
2 - mysql password and
3 - database name (no argument validation needed)
It must use the module MySQLdb (import MySQLdb)
It connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be displayed as they are
Your code should not be executed when imported
"""

import MySQLdb
import sys

if __name__ == "__main__":  # to not execute code when imported
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()  # lets U execute all d queries you need
    cursor.execute("SELECT cities.id, cities.name, states.name\
              FROM cities JOIN states ON cities.state_id = states.id\
              ORDER BY id ASC")
    for data in cursor.fetchall():  # prints d 1st cell of all rows
        print(data)
    cursor.close()
    db.close()
