#!/usr/bin/bash
import MySQLdb
import sys

def list_states(mysql_username, mysql_password, database_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
        )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
    
if __name == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(mysql_username, mysql_password, database_name)
