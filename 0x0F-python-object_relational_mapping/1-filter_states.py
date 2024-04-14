#!/usr/bin/pytho3
"""
Lists all states from database hbtn_0e_0_usa
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
    currsor.execute(
        """SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id;""")
    for row in currsor.fetchall():
        print(row)
