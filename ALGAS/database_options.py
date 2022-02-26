from enum import Enum

class DatabaseOptions(int, Enum):
    VIEW_DATA, SELECT_DATA, INSERT_DATA, DELETE_DATA, DROP_TABLE, QUIT = range(1, 7)