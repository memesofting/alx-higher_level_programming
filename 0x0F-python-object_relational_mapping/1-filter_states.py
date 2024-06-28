#!/usr/bin/python3
"""filters states starting with 'N' from the database hbtn_0c_0_usa"""
import MySQLdb
import sys


def filter_states(mysql_username, mysql_password, database_name):
    """filters states starting with 'N' from the database hbtn_0c_0_usa"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY "
                   "name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
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
    filter_states(mysql_username, mysql_password, database_name)
