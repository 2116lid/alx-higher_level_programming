#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
              (sys.argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
