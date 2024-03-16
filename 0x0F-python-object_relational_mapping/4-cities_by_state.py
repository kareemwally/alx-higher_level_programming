#!/usr/bin/python3
""" a module to connect to a localhost db and search for a state name """
import MySQLdb
import sys


def main():
    """ the main function to execute SQL query """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute("SELECT {0}.id,{0}.name,{1}.name\
        FROM {0}\
        INNER JOIN {1} ON {0}.state_id = {1}.id\
        ORDER BY cities.id ASC;".format("cities", "states"))
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
