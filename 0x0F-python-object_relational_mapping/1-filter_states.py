#!/usr/bin/python3
"""ists all states with a name starting with N (upper N) from the database"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )
    curr = db.cursor()
    curr.execute(
            "SELECT id, name FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY id ASC"
            )
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    db.close()
    