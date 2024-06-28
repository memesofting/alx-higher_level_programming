#!/usr/bin/python3
"""Filter states by user input"""
import MySQLdb
import sys

def filter_states_by_name(mysql_username, mysql_password, db_name, state_name):
    """function filters states in database by name"""
    