#!/usr/bin/python3
"""
Lists all cities from state
in hbtn_0e_4_usa
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
    query = "SELECT cities.name\
             FROM cities JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name = %s"
    cursor = db.cursor()
    cursor.execute(query, (argv[4], ))
    cities = []
    for city in cursor.fetchall():
        cities.append(city[0])
    print(", ".join(cities))
    cursor.close()
    db.close()
