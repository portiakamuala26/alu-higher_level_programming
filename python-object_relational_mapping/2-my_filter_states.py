#!/usr/bin/python3
"""Lists states matching user input from hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
