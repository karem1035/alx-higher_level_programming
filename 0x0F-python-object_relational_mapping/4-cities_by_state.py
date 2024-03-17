#!/usr/bin/python3
""" takes in an argument and displays all values matches the argument. """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establishing connection
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    # Creating a cursor
    cursor = conn.cursor()

    # Executing the query
    cursor.execute(f"SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id")

    # Fetching and printing the retrieved data
    data = cursor.fetchall()
    for i in data:
        print(i)

    # Cleaning the process
    cursor.close()
    conn.close()
