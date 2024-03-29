#!/usr/bin/python3
''' a python script to connect to a localhost db'''
import MySQLdb
import sys


def main():
    ''' the main function'''
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute("USE {0};".format(sys.argv[3]))
    cur.execute(
        "SELECT * FROM {0} ORDER BY {1} ASC;"
        .format('states', 'states.id')
        )
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
