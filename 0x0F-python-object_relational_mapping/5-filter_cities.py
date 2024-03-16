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
    cur.execute(
        "SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = '{}'\
        ORDER BY cities.id ASC;".format(sys.argv[4]))
    res = cur.fetchall()
    final = list(i[0] for i in res)
    print(*final, sep=", ")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
