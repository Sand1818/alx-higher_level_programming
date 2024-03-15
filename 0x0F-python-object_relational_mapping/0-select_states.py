#!/usr/bin/python3
""" lists all states from a database"""

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
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    db.close()
    