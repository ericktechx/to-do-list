# Importando MySQL
import mysql.connector

# Conectar-se ao servidor MySQL
meubd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0723",
    # database = "tarefas"
)

# Cursor do Banco de Dados
cursor = meubd.cursor()

# Criando o Banco de Dados
cursor.execute("CREATE DATABASE tarefas")

# Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        descricao VARCHAR(255), 
        concluido BOOLEAN
    )
""")
