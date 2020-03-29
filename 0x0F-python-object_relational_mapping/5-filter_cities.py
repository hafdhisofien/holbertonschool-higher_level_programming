#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id WHERE states.name LIKE %s ORDER BY cities.id", (argv[4],))
    query_rows = cursor.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cursor.close()
    db.close()
