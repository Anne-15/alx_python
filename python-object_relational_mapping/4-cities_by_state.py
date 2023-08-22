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
query = "SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id"
cur.execute(query)
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
