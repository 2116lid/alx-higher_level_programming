#!/usr/bin/python3
""" a python script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = conn.cursor()
c.execute("SELECT * FROM `states`")
query_rows = c.fetchall()
for state in query_rows:
    print(state)
