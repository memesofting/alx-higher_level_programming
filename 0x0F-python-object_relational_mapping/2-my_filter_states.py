#!/usr/bin/python3
"""Filter states by user input"""
import MySQLdb
import sys


def filter_states_by_name(mysql_username, mysql_password, db_name, state_name):
    """function filters states in database by name"""

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} mysql_username mysql_password "
              "database_name filter_state".
              format(sys.argv[0]))
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    filter_states_by_name(mysql_username, mysql_password, db_name, state_name)
