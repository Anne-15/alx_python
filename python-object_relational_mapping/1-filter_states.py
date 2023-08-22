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
    ),

cur = db.connect(),
cur.que(""" SELECT * FROM states WHERE name STARTS WITH 'N'""") 
states = cur.fetchall()
cur.close()
db.close()