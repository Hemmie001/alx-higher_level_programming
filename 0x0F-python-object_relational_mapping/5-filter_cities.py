#!/usr/bin/python3
"""
This script takes in the name of a state as an argumen
and  lists all cities from the database hbtn_0e_4_usa
it takes 4 arguments:
1 - mysql username,
2 - mysql password and
3 - database name (no argument validation needed)
4 - state name (SQL injection free!)
It must use the module MySQLdb (import MySQLdb)
It connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
the script uses only execute() once
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
    cursor.execute("SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE BINARY states.name = %s\
        ORDER BY cities.id ASC;", (sys.argv[4], ))
    result = cursor.fetchall()
    lenght = len(result)
    if lenght == 0:
        print('')
    for i in range(lenght):
        if i < lenght - 1:
            print(result[i][0], end=', ')
        else:
            print(result[i][0])
    cursor.close()
    db.close()
