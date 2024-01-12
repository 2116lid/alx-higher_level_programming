#!/usr/bin/python3
""" a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":

    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = con.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    q = c.fetchall()
    for state in q:
        if state[1][0] == "N":
            print(state)
