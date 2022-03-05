from enum import Enum

class DatabaseOptions(int, Enum):
    VIEW_DATA, SELECT_DATA, INSERT_DATA, DELETE_DATA, DROP_TABLE, EXPORT_CSV, EXPORT_JSON, QUIT = range(1, 9)