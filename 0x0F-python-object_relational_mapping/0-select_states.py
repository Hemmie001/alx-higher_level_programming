#!/usr/bin/python3
"""
This script lists all states from the database 'hbtn_0e_0_usa'
it takes 3 arguments:
1 - mysql username,
2 - mysql password and
3 - database name (no argument validation needed)
It must use the module MySQLdb (import MySQLdb)
It connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":  # makes code not to execute when imported
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()  # creates a cursur-lets you execute queries
    cursor.execute("SELECT * FROM states")  # Use all the SQL u like

    # print all the first cell of all the rows
    for data in cursor.fetchall():
        print(data)
    cursor.close()

    db.close()i
