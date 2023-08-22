"""
Importing MYSQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username, 
        password=password, 
        database=database, 
        port=3306
        ),

    cur = db.cursor(),
    cur.que(""" SELECT * FROM states ORDER BY id""") 
    states = cur.fetchall()
    for state in states:
        print(states)
    cur.close()
    db.close()