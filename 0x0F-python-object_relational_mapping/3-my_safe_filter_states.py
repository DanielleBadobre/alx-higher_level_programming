#!/usr/bin/python3
""" takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, but safe from injections. """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    state = sys.argv[4] + '%'
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
