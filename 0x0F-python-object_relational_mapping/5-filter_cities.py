#!/usr/bin/python3
"""takes name of a state as an argument and lists all cities of that state"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    stateName = sys.argv[4]
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC"
    cursor.execute(query, (stateName,))
    rows = cursor.fetchall()
    citiesName = [row[0] for row in rows]
    print(", ".join(citiesName))
    cursor.close()
    db.close()
