#!/usr/bin/python3
''' a python script to connect to a localhost db'''
import MySQLdb
import sys


def main():
    ''' the main function to excute sql query'''
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3]
        )
    cur = db.cursor()  # creating the obj to handle queries
    cur.execute("USE {0};".format(sys.argv[3]))  # whatever db you choose
    cur.execute(
        "SELECT * FROM {0}\
        WHERE {1} LIKE 'N%'\
        ORDER BY {2} ASC;"
        .format("states", "states.name", "states.id")
        )
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
