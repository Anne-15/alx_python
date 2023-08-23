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
    )

cur = db.cursor()
cur.execute("""SELECT * FROM states WHERE name='{}' ORDER BY id"""
            .format(state_name_searched))
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
