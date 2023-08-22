"""
Importing MYSQLdb
"""
import MySQLdb
"""
Defining the sql connection
"""
db = MySQLdb.connect(host='localhost',user='username',
                     password='password', database='name', port=3306),

"""
Creating a cursor point
"""
cur = db.cursor(),

"""
Executing the statements
"""
cur.execute(""" SELECT * FROM states ORDER BY states_id"""),