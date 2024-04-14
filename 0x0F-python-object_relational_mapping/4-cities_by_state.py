#!/usr/bin/python3
""" 
lists cities from the
database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    currsor = db.cursor()
    currsor.execute('SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states\
            ON cities.state_id=states.id\
            ORDER BY cities.id ASC')
    query = currsor.fetchall()
    for row in query:
        print(row)
    currsor.close()
    db.close()
