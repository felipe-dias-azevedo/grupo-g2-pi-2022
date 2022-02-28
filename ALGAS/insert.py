from sqlite3 import Connection, Cursor
from sql_commands import DELETE_QUERY, DELETE_QUERY_LITE, INSERT_QUERY, INSERT_QUERY_LITE

def get_insert_query(sqlite: bool):
    if not sqlite:
        return INSERT_QUERY
    else:
        return INSERT_QUERY_LITE

def insert_one(cursor: Cursor, data: tuple, sqlite: bool = False):
    insert = get_insert_query(sqlite=sqlite)
    
    cursor.execute(insert, data)

def insert_data(connection: Connection, data: list, sqlite: bool = False):
    cursor = connection.cursor()

    insert = get_insert_query(sqlite=sqlite)

    for value in data:
        cursor.execute(insert, value)

    connection.commit()

def delete_data(connection: Connection, sqlite: bool = False):
    cursor = connection.cursor()
    if not sqlite:
        cursor.execute(DELETE_QUERY)
    else:
        cursor.execute(DELETE_QUERY_LITE)
    connection.commit()
    