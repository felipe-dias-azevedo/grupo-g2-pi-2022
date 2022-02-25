from sqlite3 import Cursor
from sql_commands import SELECT_QUERY, SELECT_QUERY_LITE

def select_data(cursor: Cursor, sqlite: bool = False):
    if not sqlite:
        cursor.execute(SELECT_QUERY)
    else:
        cursor.execute(SELECT_QUERY_LITE)
    return cursor.fetchall()
