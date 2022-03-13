DATABASE_LITE = "sql-g2.db"
CREATE_QUERY_LITE = "CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, valor INTEGER, espacoMemoria INTEGER, tempoExecucao INTEGER)"
INSERT_QUERY_LITE = "INSERT INTO dados (valor, espacoMemoria, tempoExecucao) VALUES (?, ?, ?)"
SELECT_QUERY_LITE = "SELECT id, valor, espacoMemoria, tempoExecucao from dados"
DELETE_QUERY_LITE = "DELETE FROM dados"

DB_HOST = "localhost"
DB_PORT = "3306"
DB_USER = "root"
DB_PASSWORD = "123mysql@"
DATABASE = "ALGAS"

CREATE_QUERY = "CREATE TABLE IF NOT EXISTS dados (id INT PRIMARY KEY AUTO_INCREMENT, valor INT, espacoMemoria INT, tempoExecucao INT)"
INSERT_QUERY = "INSERT INTO dados (id, valor, espacoMemoria, tempoExecucao) VALUES (default, %s, %s, %s)"
SELECT_QUERY = "SELECT id, valor, espacoMemoria, tempoExecucao FROM dados"
DELETE_QUERY = "TRUNCATE dados"

DROP_QUERY = "DROP TABLE dados"
