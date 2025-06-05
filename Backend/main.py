import sqlite3
import datetime
def conectar():
    return sqlite3.connect('academico.db')
def menu():
    print("\n--- Sistema Acadêmico ---")
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Professor")
    print("3 - Cadastrar Curso")
    print("4 - Cadastrar Disciplina")
    print("5 - Cadastrar Nota")
    print("6 - Listar Alunos")
    print("7 - Listar Professores")
    print("8 - Listar Cursos")
    print("9 - Listar Disciplinas")
    print("10 - Listar Notas")
    print("11 - Verificar Aprovação de Aluno")
    print("12 - Relatório de Alunos por Curso")
    print("13 - Relatório de Alunos por Disciplina")
    print("14 - Relatório Detalhado de Aluno")
    print("15 - Verificar Conclusão de Curso")
    print("0 - Sair")
    return input("Escolha uma opção: ")
def cadastrar_aluno():
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    curso_id = input("ID do curso: ")
    conn = conectar()
    conn.execute("INSERT INTO alunos (matricula, nome, curso_id) VALUES (?, ?, ?)", (matricula, nome, curso_id))
    conn.commit()
    conn.close()
    print("Aluno cadastrado com sucesso!")
def cadastrar_professor():
    matricula = input("Matrícula do professor: ")
    nome = input("Nome do professor: ")
    curso_id = input("ID do curso: ")
    disciplina_id = input("ID da disciplina: ")
    conn = conectar()
    conn.execute("INSERT INTO professores (matricula, nome, curso_id, disciplina_id) VALUES (?, ?, ?, ?)", 
                 (matricula, nome, curso_id, disciplina_id))
    conn.commit()
    conn.close()
    print("Professor cadastrado com sucesso!")
def cadastrar_disciplina():
    codigo = input("Código da disciplina: ")
    nome = input("Nome da disciplina: ")
    conn = conectar()
    conn.execute("INSERT INTO disciplinas (codigo, nome) VALUES (?, ?)", (codigo, nome))
    conn.commit()
    conn.close()
    print("Disciplina cadastrada com sucesso!")    
def cadastrar_curso():
    codigo = input("Código do curso: ")
    nome = input("Nome do curso: ")
    conn = conectar()
    conn.execute("INSERT INTO cursos (codigo, nome) VALUES (?, ?)", (codigo, nome))
    conn.commit()
    conn.close()
    print("Curso cadastrado com sucesso!")
def cadastrar_nota():
    aluno_matricula = input("Matrícula do aluno: ")
    disciplina_codigo = input("Código da disciplina: ")
    nota = float(input("Nota: "))
    conn = conectar()
    conn.execute("INSERT INTO notas (aluno_matricula, disciplina_codigo, nota) VALUES (?, ?, ?)", 
                 (aluno_matricula, disciplina_codigo, nota))
    conn.commit()
    conn.close()
    print("Nota cadastrada com sucesso!")
def listar_alunos():
    conn = conectar()
    alunos = conn.execute("SELECT matricula, nome, curso_id FROM alunos").fetchall()
    for a in alunos:
        print(f"Matrícula: {a[0]}, Nome: {a[1]}, ID do Curso: {a[2]}")
    conn.close()
def listar_professores():
    conn = conectar()
    professores = conn.execute("SELECT matricula, nome, curso_id, disciplina_id FROM professores").fetchall()
    for p in professores:
        print(f"Matrícula: {p[0]}, Nome: {p[1]}, ID do Curso: {p[2]}, ID da Disciplina: {p[3]}")
    conn.close()
def listar_disciplinas():
    conn = conectar()
    disciplinas = conn.execute("SELECT codigo, nome FROM disciplinas").fetchall()
    for d in disciplinas:
        print(f"Código: {d[0]}, Nome: {d[1]}")
    conn.close()
def listar_cursos():
    conn = conectar()
    cursos = conn.execute("SELECT id, codigo, nome FROM cursos").fetchall()
    for c in cursos:
        print(f"ID: {c[0]}, Código: {c[1]}, Nome: {c[2]}")
    conn.close()
def listar_notas():
    conn = conectar()
    notas = conn.execute("SELECT aluno_matricula, disciplina_codigo, nota FROM notas").fetchall()
    for n in notas:
        print(f"Matrícula do Aluno: {n[0]}, Código da Disciplina: {n[1]}, Nota: {n[2]}")
    conn.close()
def verificar_aprovacao_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    conn = conectar()
    notas = conn.execute("SELECT disciplina_codigo, nota FROM notas WHERE aluno_matricula = ?", (matricula,)).fetchall()
    if not notas:
        print("Nenhuma nota encontrada para este aluno.")
        conn.close()
        return
    media = sum([n[1] for n in notas]) / len(notas)
    print(f"Média do aluno: {media:.2f}")
    if media >= 7:
        print("Aluno aprovado!")
    elif 4 <= media < 7:
        print("Aluno em recuperação.")
        disciplinas_abaixo = [n for n in notas if n[1] < 7]
        print("Disciplinas com nota abaixo de 7:")
        for d in disciplinas_abaixo:
            print(f"Disciplina: {d[0]}, Nota: {d[1]}")
        alterar = input("Deseja alterar alguma nota? (s/n): ").lower()
        if alterar == "s":
            for d in disciplinas_abaixo:
                nova_nota = float(input(f"Nova nota para {d[0]} (atual: {d[1]}): "))
                conn.execute("UPDATE notas SET nota = ? WHERE aluno_matricula = ? AND disciplina_codigo = ?", (nova_nota, matricula, d[0]))
            conn.commit()
            print("Notas atualizadas!")
    else:
        print("Aluno reprovado no curso.")
    conn.close()
def relatorio_alunos_por_curso():
    conn = conectar()
    cursos = conn.execute("SELECT id, nome FROM cursos").fetchall()
    for curso in cursos:
        print(f"\nCurso: {curso[1]} (ID: {curso[0]})")
        alunos = conn.execute("SELECT matricula, nome FROM alunos WHERE curso_id = ?", (curso[0],)).fetchall()
        if alunos:
            for a in alunos:
                print(f"  Matrícula: {a[0]}, Nome: {a[1]}")
        else:
            print("  Nenhum aluno matriculado.")
    conn.close()
def relatorio_alunos_por_disciplina():
    conn = conectar()
    disciplinas = conn.execute("SELECT codigo, nome FROM disciplinas").fetchall()
    for disc in disciplinas:
        print(f"\nDisciplina: {disc[1]} (Código: {disc[0]})")
        alunos = conn.execute("""
            SELECT a.matricula, a.nome
            FROM alunos a
            JOIN notas n ON a.matricula = n.aluno_matricula
            WHERE n.disciplina_codigo = ?
        """, (disc[0],)).fetchall()
        if alunos:
            for a in alunos:
                print(f"  Matrícula: {a[0]}, Nome: {a[1]}")
        else:
            print("  Nenhum aluno matriculado nesta disciplina.")
    conn.close()
def relatorio_detalhado_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    conn = conectar()
    aluno = conn.execute("""
        SELECT a.nome, c.nome
        FROM alunos a
        JOIN cursos c ON a.curso_id = c.id
        WHERE a.matricula = ?
    """, (matricula,)).fetchone()
    if not aluno:
        print("Aluno não encontrado.")
        conn.close()
        return
    print(f"\nAluno: {aluno[0]}")
    print(f"Curso: {aluno[1]}")
    notas = conn.execute("""
        SELECT d.nome, n.nota
        FROM notas n
        JOIN disciplinas d ON n.disciplina_codigo = d.codigo
        WHERE n.aluno_matricula = ?
    """, (matricula,)).fetchall()
    if notas:
        print("Disciplinas e notas:")
        for d in notas:
            print(f"  {d[0]}: {d[1]}")
    else:
        print("Nenhuma nota cadastrada para este aluno.")
    conn.close()
def verificar_conclusao_curso():
    matricula = input("Digite a matrícula do aluno: ")
    conn = conectar()
    # Busca todas as notas do aluno com nota >= 7
    aprovadas = conn.execute("""
        SELECT COUNT(*)
        FROM notas
        WHERE aluno_matricula = ? AND nota >= 7
    """, (matricula,)).fetchone()[0]
    if aprovadas >= 10:
        print(f"Aluno aprovado em {aprovadas} disciplinas. Curso concluído!")
        # Aqui você pode emitir o certificado, se quiser
    else:
        print(f"Aluno aprovado em {aprovadas} disciplinas. Ainda não concluiu o curso.")
    aprovadas = conn.execute("""
        SELECT COUNT(*)
        FROM notas
        WHERE aluno_matricula = ? AND nota >= 7
    """, (matricula,)).fetchone()[0]
    if aprovadas >= 10:
        aluno = conn.execute("""
            SELECT a.nome, c.nome
            FROM alunos a
            JOIN cursos c ON a.curso_id = c.id
            WHERE a.matricula = ?
        """, (matricula,)).fetchone()
        if aluno:
            data_emissao = datetime.date.today().strftime("%d/%m/%Y")
            print("\n--- CERTIFICADO DE CONCLUSÃO DE CURSO ---")
            print(f"Aluno: {aluno[0]}")
            print(f"Curso: {aluno[1]}")
            print(f"Data de emissão: {data_emissao}")
            print("-----------------------------------------\n")
        else:
            print("Aluno não encontrado para emissão do certificado.")
    else:
        print(f"Aluno aprovado em {aprovadas} disciplinas. Ainda não concluiu o curso.")
    conn.close()
if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            cadastrar_curso()
        elif opcao == "4":
            cadastrar_disciplina()
        elif opcao == "5":
            cadastrar_nota()
        elif opcao == "6":
            listar_alunos()
        elif opcao == "7":
            listar_professores()
        elif opcao == "8":
            listar_cursos()
        elif opcao == "9":
            listar_disciplinas()
        elif opcao == "10":
            listar_notas()
        elif opcao == "11":
            verificar_aprovacao_aluno()
        elif opcao == "12":
            relatorio_alunos_por_curso()
        elif opcao == "13":
            relatorio_alunos_por_disciplina()
        elif opcao == "14":
            relatorio_detalhado_aluno()
        elif opcao == "15":
            verificar_conclusao_curso()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")