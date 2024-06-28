#!/usr/bin/python3
"""script takes argument to filter query"""
import sys
import MySQLdb


def safe_filter(mysql_username, mysql_password, db_name, state_name):
    """safe filter query"""

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    for state in result:
        print(state)
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
    safe_filter(mysql_username, mysql_password, db_name, state_name)
