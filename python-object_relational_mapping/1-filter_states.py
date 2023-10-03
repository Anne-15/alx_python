#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    try:
        cursor.execute("""SELECT * FROM states WHERE name \
                       LIKE 'N%' ORDER BY id;""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        db.close()
