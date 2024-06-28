#!/usr/bin/python3
"""list all states from database"""
import sys
import MySQLdb


def list_cities(mysql_username, mysql_password, db_name):
    """list cities from database"""

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    result = cursor.fetchall()
    for city in result:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} mysql_username mysql_password db_name")
        sys.exit()
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    list_cities(mysql_username, mysql_password, db_name)
