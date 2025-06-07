import sqlite3

def criar_tabelas(): # Função para criar as tabelas no banco de dados
    conn = sqlite3.connect('academico.db')
    with open('schema.sql', 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.close()
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas() # Para criar as tabelas, execute este script uma vez.