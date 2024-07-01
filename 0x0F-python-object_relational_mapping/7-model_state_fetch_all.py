#!/usr/bin/python3
"""Script lists all state Objects from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
import urllib.parse


def all_states(mysql_username, mysql_password, db_name):
    """list all states using sqlalchemy"""

    mysql_username = urllib.parse.quote_plus(mysql_username)
    mysql_password = urllib.parse.quote_plus(mysql_password)
    db_name = urllib.parse.quote_plus(db_name)

    connection_string = f'''mysql+mysqldb://{mysql_username}:
    {mysql_password}@localhost:3306/{db_name}'''

    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} "
              "mysql_username mysql_password db_name")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    all_states(mysql_username, mysql_password, db_name)
