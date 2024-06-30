#!/usr/bin/python3
"""Script lists all state Objects from database"""
import SQLAlchemy as sa
import MySQLdb
from model_state import Base, State
import sys


def all_states(mysql_username, mysql_password, db_name):
    """list all states using sqlalchemy"""

    connection_string = f'''mysql+mysqldb://
    {mysql_username}:{mysql_password}@localhost:3306/{db_name}'''
    engine = sa.create_engine(connection_string)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} "
              "mysql_username mysql_password db_name")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    all_states(mysql_username, mysql_password, db_name)
