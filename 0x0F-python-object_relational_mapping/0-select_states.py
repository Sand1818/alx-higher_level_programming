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
        password=sys.argv[2],
        db=sys.argv[3])

    currs = db.cursor()
    currs.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in currs.fetchall():
        print(state)
    currs.close()
    db.close()
