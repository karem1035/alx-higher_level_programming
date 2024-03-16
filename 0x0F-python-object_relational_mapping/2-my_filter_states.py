#!/usr/bin/python3
""" takes in an argument and displays all values matches the argument. """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[2]
    password = sys.argv[2]
    database = sys.argv[3]
    namearg = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY '{}'\
                    ORDER BY id ASC".format(namearg))

    data = cursor.fetchall()
    for i in data:
        print(i)

    cursor.close()
    conn.close()
