from sqlite3 import Cursor, connect as connect_lite
from sql_commands import CREATE_QUERY_LITE, DATABASE, CREATE_QUERY, DATABASE_LITE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER, DROP_QUERY
from mysql.connector import connect as connect_my

def get_connection(sqlite: bool = False):
    if not sqlite:
        return connect_my(
            # host = DB_HOST + ":" + DB_PORT,
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DATABASE
        )
    else:
        return connect_lite(DATABASE_LITE)

def create_db(sqlite: bool = False):
    con = get_connection(sqlite)
    c = con.cursor()
    if not sqlite:
        c.execute(CREATE_QUERY)
    else:
        c.execute(CREATE_QUERY_LITE)
    return con

def drop_table_db(cursor: Cursor):
    cursor.execute(DROP_QUERY)
