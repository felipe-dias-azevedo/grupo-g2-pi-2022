from typing import Dict, List
from mysql.connector import connect as connect_my

RAW_TABLE = "dados"

PROCESSED_TABLE = "analytics"


def get_create_table_query(raw: bool):
    int_or_text = 'INT' if raw else 'TEXT'
    bool_or_text = 'BOOLEAN' if raw else 'TEXT'
    return "CREATE TABLE IF NOT EXISTS " \
           f"{RAW_TABLE if raw else PROCESSED_TABLE} (" \
           "id INT PRIMARY KEY AUTO_INCREMENT, " \
           "mensalidade INT, " \
           "estado TEXT, " \
           "municipio TEXT, " \
           "nome_curso TEXT, " \
           "quantidade_bolsas INT, " \
           "nota_bolsa INT, " \
           f"sexo {int_or_text}, " \
           f"raca {int_or_text}, " \
           f"deficiente {bool_or_text}, " \
           "idade INT, " \
           f"esgoto_inexistente {bool_or_text}, " \
           f"energia_eletrica_inexistente {bool_or_text}, " \
           f"agua_inexistente {bool_or_text}, " \
           f"acesso_internet {bool_or_text}, " \
           f"faz_exame_selecao {bool_or_text}, " \
           f"especializada_deficientes {bool_or_text}, " \
           f"ensino_tecnico {bool_or_text}, " \
           "espaco_memoria INT, " \
           "tempo_execucao INT" \
           ")"


def get_insert_query(raw: bool):
    return "INSERT INTO " \
           f"{RAW_TABLE if raw else PROCESSED_TABLE} " \
           "(id, mensalidade, estado, municipio, nome_curso, quantidade_bolsas, nota_bolsa, sexo, raca, " \
           "deficiente, idade, esgoto_inexistente, energia_eletrica_inexistente, agua_inexistente, " \
           "acesso_internet, faz_exame_selecao, especializada_deficientes, ensino_tecnico, espaco_memoria, " \
           "tempo_execucao) " \
           "VALUES " \
           "(default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


def get_select_query(raw: bool):
    return "SELECT " \
           "id, mensalidade, estado, municipio, nome_curso, quantidade_bolsas, nota_bolsa, sexo, raca, " \
           "deficiente, idade, esgoto_inexistente, energia_eletrica_inexistente, agua_inexistente, " \
           "acesso_internet, faz_exame_selecao, especializada_deficientes, ensino_tecnico, espaco_memoria, " \
           "tempo_execucao " \
           "FROM " \
           f"{RAW_TABLE if raw else PROCESSED_TABLE}"


def get_delete_query(raw: bool):
    return f"TRUNCATE {RAW_TABLE if raw else PROCESSED_TABLE}"


class DatabaseManager:
    connection = None

    def __init__(self, host: str, user: str, password: str, database: str):
        self.connection = connect_my(host=host, user=user, password=password, database=database)
        self.create(raw=False)
        self.create(raw=True)

    def create(self, raw: bool):
        cursor = self.connection.cursor()
        cursor.execute(get_create_table_query(raw=raw))
        cursor.close()

    def insert(self, data: List[Dict], raw: bool):
        cursor = self.connection.cursor()
        for value in data:
            cursor.execute(get_insert_query(raw=raw), tuple(value.values()))
        self.connection.commit()
        cursor.close()

    def select(self, raw: bool):
        cursor = self.connection.cursor()
        cursor.execute(get_select_query(raw=raw))
        fields = [field_md[0] for field_md in cursor.description]
        values = [dict(zip(fields, row)) for row in cursor.fetchall()]
        cursor.close()
        return values

    def delete(self, raw: bool):
        cursor = self.connection.cursor()
        cursor.execute(get_delete_query(raw=raw))
        self.connection.commit()
        cursor.close()
