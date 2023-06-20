#!/usr/bin/python3
"""
This  script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
it takes 4 arguments:
1 - mysql username,
2 - mysql password and
3 - database name
4 - state name searched (safe from MySQL injection)
It must use the module MySQLdb (import MySQLdb)
It connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":  # to not execute code when imported
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()  # lets U execute all d queries you need
    cursor.execute("SELECT * FROM states WHERE name = %(name)s",
                   {'name': argv[4]})
    for data in cursor.fetchall():  # prints d 1st cell of all rows
        print(data)
    cursor.close()
    db.close()
