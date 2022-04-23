from typing import Dict, List
from mysql.connector import connect as connect_my


CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS " \
               "dados (" \
               "id INT PRIMARY KEY AUTO_INCREMENT, " \
               "mensalidade INT, " \
               "estado TEXT, " \
               "municipio TEXT, " \
               "nome_curso TEXT, " \
               "quantidade_bolsas INT, " \
               "nota_bolsa INT, " \
               "sexo INT, " \
               "raca INT, " \
               "deficiente BOOLEAN, " \
               "idade INT, " \
               "esgoto_inexistente BOOLEAN, " \
               "energia_eletrica_inexistente BOOLEAN, " \
               "agua_inexistente BOOLEAN, " \
               "acesso_internet BOOLEAN, " \
               "faz_exame_selecao BOOLEAN, " \
               "especializada_deficientes BOOLEAN, " \
               "ensino_tecnico BOOLEAN, " \
               "espaco_memoria INT, " \
               "tempo_execucao INT" \
               ")"

INSERT_QUERY = "INSERT INTO " \
              "dados " \
              "(id, mensalidade, estado, municipio, nome_curso, quantidade_bolsas, nota_bolsa, sexo, raca, deficiente, idade, esgoto_inexistente, energia_eletrica_inexistente, agua_inexistente, acesso_internet, faz_exame_selecao, especializada_deficientes, ensino_tecnico, espaco_memoria, tempo_execucao) " \
              "VALUES " \
              "(default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

SELECT_QUERY = "SELECT " \
               "id, mensalidade, estado, municipio, nome_curso, quantidade_bolsas, nota_bolsa, sexo, raca, deficiente, idade, esgoto_inexistente, energia_eletrica_inexistente, agua_inexistente, acesso_internet, faz_exame_selecao, especializada_deficientes, ensino_tecnico, espaco_memoria, tempo_execucao " \
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

    def insert(self, data: List[Dict]):
        cursor = self.connection.cursor()
        for value in data:
            cursor.execute(INSERT_QUERY, tuple(value.values()))
        self.connection.commit()
        cursor.close()

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute(SELECT_QUERY)
        fields = [field_md[0] for field_md in cursor.description]
        values = [dict(zip(fields,row)) for row in cursor.fetchall()]
        cursor.close()
        return values

    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute(DELETE_QUERY)
        self.connection.commit()
        cursor.close()
