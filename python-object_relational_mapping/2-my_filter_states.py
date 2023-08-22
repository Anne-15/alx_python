"""
Importing MYSQLdb
"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name_searched = sys.argv[4]

db = MySQLdb.connect(
    host='localhost',
    user=username, 
    password=password, 
    database=database, 
    port=3306
    ),

cur = db.connect(),
cur.que(""" SELECT * FROM states WHERE name IS EQUAL TO ${state_name_searched} ORDER BY id""") 
states = cur.fetchall()
cur.close()
db.close()