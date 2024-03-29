#!/usr/bin/python3

"""
return info from both tables (tables 'cities' 'states)
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    sql_cmd = """SELECT cities.id, cities.name, states.name
                 FROM states JOIN cities
                 WHERE cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    cursor.execute(sql_cmd)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
