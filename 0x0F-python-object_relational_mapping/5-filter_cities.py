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
    cursor.execute(f"SELECT cities.name FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name = '{argv[4]}'")

    # Fetching and printing the retrieved data
    data = cursor.fetchall()
    output = []
    for i in data:
        output.append(i[0])
    print(', '.join(output))

    # Cleaning the process
    cursor.close()
    conn.close()
