"""
Importing MYSQLdb
"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host='localhost',
    user=username, 
    password=password, 
    database=database, 
    port=3306
    )

cur = db.cursor()
cur.execute(""" SELECT * FROM states WHERE name STARTS WITH 'N'""") 
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()