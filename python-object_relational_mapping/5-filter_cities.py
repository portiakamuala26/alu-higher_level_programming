#!/usr/bin/python3
"""Lists all cities of a state from hbtn_0e_4_usa."""

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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (sys.argv[4],))

    cities = cursor.fetchall()

    city_names = []

    for city in cities:
        city_names.append(city[0])

    print(", ".join(city_names))

    cursor.close()
    db.close()
