#!/usr/bin/python3
"""list all states from database by state"""
import sys
import MySQLdb


def list_cities_by_state(mysql_username, mysql_password, db_name, state_name):
    """list cities from database by state"""

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = %s
    ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    city = [cities[0] for cities in result]
    print(", ".join(city))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} mysql_username mysql_password "
              "db_name state_name")
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    list_cities_by_state(mysql_username, mysql_password, db_name, state_name)
