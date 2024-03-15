#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa where name matches the argument"""

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
    curr.execute('SELECT * FROM states\
            WHERE states.name=%s\
            ORDER BY states.id ASC', (sys.argv[4],))
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    db.close()
    