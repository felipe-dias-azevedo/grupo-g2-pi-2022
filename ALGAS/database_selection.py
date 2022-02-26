from enum import Enum

class DatabaseSelection(int, Enum):
    SQLITE, MYSQL = range(1, 3)