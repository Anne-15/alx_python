"""
Importing MYSQLdb
"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

db = MySQLdb.connect(
    host='localhost',
    user=username,
    password=password,
    database=database,
    port=3306
    )

cur = db.cursor()
query = "SELECT states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name='{}' \
                 ORDER BY cities.id"
cur.execute(query, (state_name))
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
db.close()
