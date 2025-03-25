# Importando MySQL
import mysql.connector

# Conectar-se ao servidor MySQL
meubd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0723",
    database = "tarefas"
)

# Cursor do Banco de Dados
cursor = meubd.cursor()

# Função para adicionar tarefa ao banco de dados
def adicionar_tarefas(i):
    sql = "INSERT INTO tarefas (descricao, concluido) VALUES(%s, %s)"
    valores = (i, False)
    cursor.execute(sql, valores)
    meubd.commit()


# Função para obter todas as tarefas do banco de dados
def obter_tarefas():
    sql = "SELECT * FROM tarefas"
    cursor.execute(sql)
    return cursor.fetchall()


# Função para marcar uma tarefa como concluida
def marcar_completo(id_tarefa):
    sql = "UPDATE tarefas SET concluido = True WHERE id = %s"
    valores = (id_tarefa,)
    cursor.execute(sql, valores)
    meubd.commit()


# Função para excluir uma tarefa do banco de dados
def deletar_tarefas(id_tarefa):
    sql = "DELETE FROM tarefas WHERE id = %s"
    valores = (id_tarefa,)
    cursor.execute(sql, valores)
    meubd.commit()
