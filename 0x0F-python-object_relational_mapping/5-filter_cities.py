#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([a[2] for a in c.fetchall() if a[4] == argv[4]]))
