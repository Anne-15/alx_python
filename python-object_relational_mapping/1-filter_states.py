#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    # Read MySQL credentials from command line arguments
    username, password, database = sys.argv[1:4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    try:
        # Execute the SQL query
        cursor.execute("""SELECT * FROM states WHERE name \
                       COLLATE Latin1_General_CS \
                       LIKE 'N%' ORDER BY id;""")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
