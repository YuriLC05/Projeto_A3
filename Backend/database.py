import sqlite3 

def conectar(): # Função para conectar ao banco de dados
    return sqlite3.connect('academico.db') # Função que retorna a conexão com o banco de dados