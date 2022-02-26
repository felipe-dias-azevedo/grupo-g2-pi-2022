from insert import insert_data, delete_data, insert_one
from create import create_db, drop_table_db
from select_data import select_data

class DatabaseManager:
    def __init__(self, sqlite: bool):
        self.is_sqlite = sqlite
        self.connection = self.create()
        self.cursor = None
    
    def create(self):
        return create_db(sqlite=self.is_sqlite)

    def transact_begin(self):
        self.cursor = self.connection.cursor()
    
    def transact_insert(self, dados: tuple):
        assert self.cursor != None, "Transaction not started"
        insert_one(self.cursor, dados, self.is_sqlite)

    def transact_commit(self):
        self.connection.commit()

    def insert(self, dados: list):
        insert_data(self.connection, dados, sqlite=self.is_sqlite)
        
    def select(self) -> list:
        return select_data(cursor=self.connection.cursor(), sqlite=self.is_sqlite)

    def delete(self):
        delete_data(connection=self.connection, sqlite=self.is_sqlite)

    def drop(self):
        drop_table_db(cursor=self.connection.cursor())