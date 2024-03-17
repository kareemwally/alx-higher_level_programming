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
    if (len(sys.argv) > 5):
        exit(1)
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC;"
    cur.execute(query.format(sys.argv[4]))
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
