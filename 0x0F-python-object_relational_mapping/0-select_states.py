#!/usr/bin/python3
"""script lists all states from the database hbtn_0c_0_usa"""
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
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} mysql_username mysql_password database_name".
              format(sys.argv[0]))
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(mysql_username, mysql_password, database_name)
