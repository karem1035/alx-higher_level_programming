#!/usr/bin/python3
#  a script that lists all states from the database hbtn_0e_0_usa:
import MySQLdb
import sys

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database = sys.argv[3]
	
	conn = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=username,
		passwd=password,
		db=database
		)

	cursor = conn.cursor()
	cursor.execute("SELECT * FROM states")
	for i in cursor:
		print(i)
