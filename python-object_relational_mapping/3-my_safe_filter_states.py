#!/usr/bin/python3
"""
Safe from MySQL injections! This script takes in arguments and displays all
values in the 'states' table of 'hbtn_0e_0_usa' where 'name' matches the
argument, but is safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
