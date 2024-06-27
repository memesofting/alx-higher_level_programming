#!/usr/bin/python3
import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name):
    """lists all states from the database hbtn_0c_0_usa"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """rows = cursor.fetchall()"""
    for row in cursor:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(mysql_username, mysql_password, database_name)
