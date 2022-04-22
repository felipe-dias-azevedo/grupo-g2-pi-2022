from mysql.connector import connect as connect_my

CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS " \
               "dados (" \
               "id INT PRIMARY KEY AUTO_INCREMENT, " \
               "valor INT, " \
               "espacoMemoria INT, " \
               "tempoExecucao INT" \
               ")"

INSERT_QUERY = "INSERT INTO " \
              "dados " \
              "(id, valor, espacoMemoria, tempoExecucao) " \
              "VALUES " \
              "(default, %s, %s, %s)"

SELECT_QUERY = "SELECT " \
               "id, valor, espacoMemoria, tempoExecucao " \
               "FROM " \
               "dados"

DELETE_QUERY = "TRUNCATE dados"


class DatabaseManager:

    connection = None

    def __init__(self, host: str, user: str, password: str, database: str):
        self.connection = connect_my(host=host, user=user, password=password, database=database)
        self.create()

    def create(self):
        cursor = self.connection.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        cursor.close()

    def insert(self, data: list[dict]):
        cursor = self.connection.cursor()
        for value in data:
            cursor.execute(INSERT_QUERY, value)
        self.connection.commit()
        cursor.close()

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute()
        values = cursor.fetchall()
        cursor.close()
        return values

    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute(DELETE_QUERY)
        self.connection.commit()
        cursor.close()
