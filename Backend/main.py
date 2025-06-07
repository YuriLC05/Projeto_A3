import sqlite3 # Função para manipulação de banco de dados SQLite	
import datetime # Biblioteca para manipulação de datas
def conectar(): # Função para conectar ao banco de dados SQLite
    return sqlite3.connect('academico.db')  # Retorna a conexão com o banco de dados
def menu(): # Função para exibir o menu principal do sistema
    print("\n--- Sistema Acadêmico ---") # Exibe o título do menu
    print("1 - Cadastrar Aluno") # Opção para cadastrar um aluno
    print("2 - Cadastrar Professor") # Opção para cadastrar um professor
    print("3 - Cadastrar Curso") # Opção para cadastrar um curso
    print("4 - Cadastrar Disciplina") # Opção para cadastrar uma disciplina
    print("5 - Cadastrar Nota") # Opção para cadastrar uma nota
    print("6 - Listar Alunos") # Opção para listar todos os alunos cadastrados
    print("7 - Listar Professores") # Opção para listar todos os professores cadastrados
    print("8 - Listar Cursos") # Opção para listar todos os cursos cadastrados
    print("9 - Listar Disciplinas") # Opção para listar todas as disciplinas cadastradas
    print("10 - Listar Notas") # Opção para listar todas as notas cadastradas
    print("11 - Verificar Aprovação de Aluno") # Opção para verificar a aprovação de um aluno com base nas notas
    print("12 - Relatório de Alunos por Curso") # Opção para gerar um relatório de alunos por curso
    print("13 - Relatório de Alunos por Disciplina") # Opção para gerar um relatório de alunos por disciplina
    print("14 - Relatório Detalhado de Aluno") # Opção para gerar um relatório detalhado de um aluno específico
    print("15 - Verificar Conclusão de Curso") # Opção para verificar se um aluno concluiu o curso
    print("16 - Emitir Certificado de Conclusão de Curso") # Opção para emitir um certificado de conclusão de curso
    print("0 - Sair") # Opção para sair do sistema
    return input("Escolha uma opção: ") # Retorna a opção escolhida pelo usuário
def cadastrar_aluno(): # Função para cadastrar um novo aluno
    matricula = input("Matrícula do aluno: ") # Solicita a matrícula do aluno
    nome = input("Nome do aluno: ") # Solicita o nome do aluno
    curso_id = input("ID do curso: ") # Solicita o ID do curso ao qual o aluno pertence
    conn = conectar() # Conecta ao banco de dados
    conn.execute("INSERT INTO alunos (matricula, nome, curso_id) VALUES (?, ?, ?)", (matricula, nome, curso_id)) # Insere os dados do aluno na tabela 'alunos'
    conn.commit() # Confirma a transação
    conn.close() # Fecha a conexão com o banco de dados
    print("Aluno cadastrado com sucesso!") # Exibe mensagem de sucesso após o cadastro
def cadastrar_professor(): # Função para cadastrar um novo professor
    matricula = input("Matrícula do professor: ") # Solicita a matrícula do professor
    nome = input("Nome do professor: ") # Solicita o nome do professor
    curso_id = input("ID do curso: ") # Solicita o ID do curso ao qual o professor pertence
    disciplina_codigo = input("Codigo da disciplina: ") # Solicita o ID da disciplina que o professor leciona
    conn = conectar() # Conecta ao banco de dados
    conn.execute("INSERT INTO professores (matricula, nome, curso_id, disciplina_codigo) VALUES (?, ?, ?, ?)", 
                 (matricula, nome, curso_id, disciplina_codigo)) # Insere os dados do professor na tabela 'professores'
    conn.commit() # Confirma a transação
    conn.close() # Fecha a conexão com o banco de dados
    print("Professor cadastrado com sucesso!") # Exibe mensagem de sucesso após o cadastro
def cadastrar_disciplina(): # Função para cadastrar uma nova disciplina
    codigo = input("Código da disciplina: ") # Solicita o código da disciplina
    nome = input("Nome da disciplina: ") # Solicita o nome da disciplina
    conn = conectar() # Conecta ao banco de dados
    conn.execute("INSERT INTO disciplinas (codigo, nome) VALUES (?, ?)", (codigo, nome)) # Insere os dados da disciplina na tabela 'disciplinas'
    conn.commit() # Confirma a transação
    conn.close() # Fecha a conexão com o banco de dados
    print("Disciplina cadastrada com sucesso!") # Exibe mensagem de sucesso após o cadastro
def cadastrar_curso(): # Função para cadastrar um novo curso
    codigo = input("Código do curso: ") # Solicita o código do curso
    nome = input("Nome do curso: ") # Solicita o nome do curso
    conn = conectar() # Conecta ao banco de dados
    conn.execute("INSERT INTO cursos (codigo, nome) VALUES (?, ?)", (codigo, nome)) # Insere os dados do curso na tabela 'cursos'
    conn.commit() # Confirma a transação
    conn.close() # Fecha a conexão com o banco de dados
    print("Curso cadastrado com sucesso!") # Exibe mensagem de sucesso após o cadastro
def cadastrar_nota(): # Função para cadastrar uma nova nota
    matricula_aluno = input("Matrícula do aluno: ") # Solicita a matrícula do aluno
    disciplina_codigo = input("Código da disciplina: ") # Solicita o código da disciplina
    nota = float(input("Nota: ")) # Solicita a nota do aluno
    conn = conectar() # Conecta ao banco de dados
    conn.execute("INSERT INTO notas (matricula_aluno, disciplina_codigo, nota) VALUES (?, ?, ?)", 
                 (matricula_aluno, disciplina_codigo, nota)) # Insere os dados da nota na tabela 'notas'
    conn.commit() # Confirma a transação
    conn.close() # Fecha a conexão com o banco de dados
    print("Nota cadastrada com sucesso!") # Exibe mensagem de sucesso após o cadastro
def listar_alunos(): # Função para listar todos os alunos cadastrados
    conn = conectar() # Conecta ao banco de dados
    alunos = conn.execute("SELECT matricula, nome, curso_id FROM alunos").fetchall() # Busca todos os alunos na tabela 'alunos'
    for a in alunos: # Itera sobre cada aluno encontrado
        print(f"Matrícula: {a[0]}, Nome: {a[1]}, ID do Curso: {a[2]}") # Exibe os dados de cada aluno
    conn.close() # Fecha a conexão com o banco de dados
def listar_professores(): # Função para listar todos os professores cadastrados
    conn = conectar() # Conecta ao banco de dados
    professores = conn.execute("SELECT matricula, nome, curso_id, disciplina_codigo FROM professores").fetchall() # Busca todos os professores na tabela 'professores'
    for p in professores: # Itera sobre cada professor encontrado
        print(f"Matrícula: {p[0]}, Nome: {p[1]}, ID do Curso: {p[2]}, ID da Disciplina: {p[3]}") # Exibe os dados de cada professor
    conn.close() # Fecha a conexão com o banco de dados
def listar_disciplinas(): # Função para listar todas as disciplinas cadastradas
    conn = conectar() # Conecta ao banco de dados
    disciplinas = conn.execute("SELECT codigo, nome FROM disciplinas").fetchall() # Busca todas as disciplinas na tabela 'disciplinas'
    for d in disciplinas: # Itera sobre cada disciplina encontrada
        print(f"Código: {d[0]}, Nome: {d[1]}") # Exibe os dados de cada disciplina
    conn.close() # Fecha a conexão com o banco de dados
def listar_cursos(): # Função para listar todos os cursos cadastrados
    conn = conectar() # Conecta ao banco de dados
    cursos = conn.execute("SELECT id, codigo, nome FROM cursos").fetchall() # Busca todos os cursos na tabela 'cursos'
    for c in cursos: # Itera sobre cada curso encontrado
        print(f"ID: {c[0]}, Código: {c[1]}, Nome: {c[2]}") # Exibe os dados de cada curso
    conn.close() # Fecha a conexão com o banco de dados
def listar_notas(): # Função para listar todas as notas cadastradas
    conn = conectar() # Conecta ao banco de dados
    notas = conn.execute("SELECT matricula_aluno, disciplina_codigo, nota FROM notas").fetchall() # Busca todas as notas na tabela 'notas'
    for n in notas: # Itera sobre cada nota encontrada
        print(f"Matrícula do Aluno: {n[0]}, Código da Disciplina: {n[1]}, Nota: {n[2]}") # Exibe os dados de cada nota
    conn.close() # Fecha a conexão com o banco de dados
def verificar_aprovacao_aluno(): # Função para verificar a aprovação de um aluno com base nas notas
    matricula = input("Digite a matrícula do aluno: ") # Solicita a matrícula do aluno
    conn = conectar() # Conecta ao banco de dados
    notas = conn.execute("SELECT disciplina_codigo, nota FROM notas WHERE matricula_aluno = ?", (matricula,)).fetchall() # Busca as notas do aluno na tabela 'notas'
    if not notas: # Verifica se o aluno possui notas cadastradas
        print("Nenhuma nota encontrada para este aluno.") # Exibe mensagem caso não haja notas
        conn.close() # Fecha a conexão com o banco de dados
        return # Retorna se não houver notas
    media = sum([n[1] for n in notas]) / len(notas) # Calcula a média das notas do aluno
    print(f"Média do aluno: {media:.2f}") # Exibe a média do aluno com duas casas decimais
    if media >= 7: # Verifica se a média é maior ou igual a 7
        print("Aluno aprovado!") # Exibe mensagem de aprovação
    elif 4 <= media < 7: # Verifica se a média está entre 4 e 7
        print("Aluno em recuperação.") # Exibe mensagem de recuperação
        disciplinas_abaixo = [n for n in notas if n[1] < 7] # Filtra as disciplinas com notas abaixo de 7
        print("Disciplinas com nota abaixo de 7:") # Exibe as disciplinas com notas abaixo de 7
        for d in disciplinas_abaixo: # Itera sobre as disciplinas com notas abaixo de 7
            print(f"Disciplina: {d[0]}, Nota: {d[1]}") # Exibe os dados de cada disciplina
        alterar = input("Deseja alterar alguma nota? (s/n): ").lower() # Pergunta se o usuário deseja alterar alguma nota
        if alterar == "s": # Se o usuário optar por alterar notas
            for d in disciplinas_abaixo: # Itera sobre as disciplinas com notas abaixo de 7
                nova_nota = float(input(f"Nova nota para {d[0]} (atual: {d[1]}): ")) # Solicita a nova nota para a disciplina
                conn.execute("UPDATE notas SET nota = ? WHERE matricula_aluno = ? AND disciplina_codigo = ?", (nova_nota, matricula, d[0])) # Atualiza a nota na tabela 'notas'
            conn.commit() # Confirma a transação
            print("Notas atualizadas!") # Exibe mensagem de sucesso após a atualização das notas
    else: # Se a média for menor que 4
        print("Aluno reprovado no curso.") # Exibe mensagem de reprovação
    conn.close() # Fecha a conexão com o banco de dados
def relatorio_alunos_por_curso(): # Função para gerar um relatório de alunos por curso
    conn = conectar() # Conecta ao banco de dados
    cursos = conn.execute("SELECT id, nome FROM cursos").fetchall() # Busca todos os cursos na tabela 'cursos'
    for curso in cursos: # Itera sobre cada curso encontrado
        print(f"\nCurso: {curso[1]} (ID: {curso[0]})") # Exibe o nome e ID do curso
        alunos = conn.execute("SELECT matricula, nome FROM alunos WHERE curso_id = ?", (curso[0],)).fetchall() # Busca os alunos matriculados no curso
        if alunos: # Verifica se há alunos matriculados no curso
            for a in alunos: # Itera sobre cada aluno encontrado
                print(f"  Matrícula: {a[0]}, Nome: {a[1]}") # Exibe os dados de cada aluno
        else: # Se não houver alunos matriculados no curso
            print("  Nenhum aluno matriculado.") # Exibe mensagem informando que não há alunos matriculados
    conn.close() # Fecha a conexão com o banco de dados
def relatorio_alunos_por_disciplina(): # Função para gerar um relatório de alunos por disciplina
    conn = conectar() # Conecta ao banco de dados
    disciplinas = conn.execute("SELECT codigo, nome FROM disciplinas").fetchall() # Busca todas as disciplinas na tabela 'disciplinas'
    for disc in disciplinas: # Itera sobre cada disciplina encontrada
        print(f"\nDisciplina: {disc[1]} (Código: {disc[0]})") # Exibe o nome e código da disciplina
        alunos = conn.execute(""" 
            SELECT a.matricula, a.nome
            FROM alunos a
            JOIN notas n ON a.matricula = n.matricula_aluno
            WHERE n.disciplina_codigo = ?
        """, (disc[0],)).fetchall() # Busca os alunos matriculados na disciplina
        if alunos: # Verifica se há alunos matriculados na disciplina
            for a in alunos: # Itera sobre cada aluno encontrado
                print(f"  Matrícula: {a[0]}, Nome: {a[1]}") # Exibe os dados de cada aluno
        else: # Se não houver alunos matriculados na disciplina
            print("  Nenhum aluno matriculado nesta disciplina.") # Exibe mensagem informando que não há alunos matriculados
    conn.close() # Fecha a conexão com o banco de dados
def relatorio_detalhado_aluno(): # Função para gerar um relatório detalhado de um aluno específico
    matricula = input("Digite a matrícula do aluno: ") # Solicita a matrícula do aluno
    conn = conectar() # Conecta ao banco de dados
    aluno = conn.execute("""
        SELECT a.nome, c.nome
        FROM alunos a
        JOIN cursos c ON a.curso_id = c.id
        WHERE a.matricula = ?
    """, (matricula,)).fetchone() # Busca os dados do aluno na tabela 'alunos' e o curso ao qual pertence
    if not aluno: # Verifica se o aluno foi encontrado
        print("Aluno não encontrado.") # Exibe mensagem caso o aluno não seja encontrado
        conn.close() # Fecha a conexão com o banco de dados
        return # Retorna se o aluno não for encontrado
    print(f"\nAluno: {aluno[0]}") # Exibe o nome do aluno
    print(f"Curso: {aluno[1]}") # Exibe o nome do curso ao qual o aluno pertence
    notas = conn.execute(""" 
        SELECT d.nome, n.nota
        FROM notas n
        JOIN disciplinas d ON n.disciplina_codigo = d.codigo
        WHERE n.matricula_aluno = ?
    """, (matricula,)).fetchall() # Busca as notas do aluno e as disciplinas correspondentes
    if notas: # Verifica se o aluno possui notas cadastradas
        print("Disciplinas e notas:") # Exibe o título da seção de disciplinas e notas
        for d in notas: # Itera sobre cada nota encontrada
            print(f"  {d[0]}: {d[1]}") # Exibe o nome da disciplina e a nota correspondente
    else: # Se o aluno não tiver notas cadastradas
        print("Nenhuma nota cadastrada para este aluno.") # Exibe mensagem informando que não há notas cadastradas
    conn.close() # Fecha a conexão com o banco de dados
def verificar_conclusao_curso(): # Função para verificar se um aluno concluiu o curso
    matricula = input("Digite a matrícula do aluno: ") # Solicita a matrícula do aluno
    conn = conectar() # Conecta ao banco de dados
    # Busca todas as notas do aluno com nota >= 7 
    aprovadas = conn.execute("""
        SELECT COUNT(*)
        FROM notas
        WHERE matricula_aluno = ? AND nota >= 7
    """, (matricula,)).fetchone()[0] # Conta quantas disciplinas o aluno foi aprovado
    if aprovadas >= 10: # Se o aluno foi aprovado em 10 ou mais disciplinas
        print(f"Aluno aprovado em {aprovadas} disciplinas. Curso concluído!") # Exibe mensagem de conclusão do curso
        # Aqui você pode emitir o certificado, se quiser
    else: # Se o aluno não foi aprovado em 10 disciplinas
        print(f"Aluno aprovado em {aprovadas} disciplinas. Ainda não concluiu o curso.") # Exibe mensagem informando que o curso não foi concluído
    aprovadas = conn.execute("""
        SELECT COUNT(*)
        FROM notas
        WHERE matricula_aluno = ? AND nota >= 7
    """, (matricula,)).fetchone()[0] # Conta quantas disciplinas o aluno foi aprovado
    if aprovadas >= 10: # Se o aluno foi aprovado em 10 ou mais disciplinas
        aluno = conn.execute("""
            SELECT a.nome, c.nome
            FROM alunos a
            JOIN cursos c ON a.curso_id = c.id
            WHERE a.matricula = ?
        """, (matricula,)).fetchone() # Busca os dados do aluno e o curso ao qual pertence
        if aluno: # Verifica se o aluno foi encontrado
            data_emissao = datetime.date.today().strftime("%d/%m/%Y") # Obtém a data atual formatada
            print("\n--- CERTIFICADO DE CONCLUSÃO DE CURSO ---") # Exibe o título do certificado
            print(f"Aluno: {aluno[0]}") # Exibe o nome do aluno
            print(f"Curso: {aluno[1]}") # Exibe o nome do curso ao qual o aluno pertence
            print(f"Data de emissão: {data_emissao}") # Exibe a data de emissão do certificado
            print("-----------------------------------------\n") # Exibe uma linha de separação
        else: # Se o aluno não for encontrado
            print("Aluno não encontrado para emissão do certificado.") # Exibe mensagem informando que o aluno não foi encontrado
    else: # Se o aluno não foi aprovado em 10 disciplinas
        print(f"Aluno aprovado em {aprovadas} disciplinas. Ainda não concluiu o curso.") # Exibe mensagem informando que o curso não foi concluído
    conn.close() # Fecha a conexão com o banco de dados
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    while True: # Loop para exibir o menu e processar as opções escolhidas pelo usuário
        opcao = menu() # Chama a função menu para exibir as opções
        if opcao == "1": # Se a opção escolhida for 1
            cadastrar_aluno() # Chama a função para cadastrar um aluno
        elif opcao == "2": # Se a opção escolhida for 2
            cadastrar_professor() # Chama a função para cadastrar um professor
        elif opcao == "3": # Se a opção escolhida for 3
            cadastrar_curso() # Chama a função para cadastrar um curso
        elif opcao == "4": # Se a opção escolhida for 4
            cadastrar_disciplina() # Chama a função para cadastrar uma disciplina
        elif opcao == "5": # Se a opção escolhida for 5
            cadastrar_nota() # Chama a função para cadastrar uma nota
        elif opcao == "6": # Se a opção escolhida for 6
            listar_alunos() # Chama a função para listar todos os alunos cadastrados
        elif opcao == "7": # Se a opção escolhida for 7
            listar_professores() # Chama a função para listar todos os professores cadastrados
        elif opcao == "8": # Se a opção escolhida for 8
            listar_cursos() # Chama a função para listar todos os cursos cadastrados
        elif opcao == "9": # Se a opção escolhida for 9
            listar_disciplinas() # Chama a função para listar todas as disciplinas cadastradas
        elif opcao == "10": # Se a opção escolhida for 10
            listar_notas() # Chama a função para listar todas as notas cadastradas
        elif opcao == "11": # Se a opção escolhida for 11
            verificar_aprovacao_aluno() # Chama a função para verificar a aprovação de um aluno com base nas notas
        elif opcao == "12": # Se a opção escolhida for 12
            relatorio_alunos_por_curso() # Chama a função para gerar um relatório de alunos por curso
        elif opcao == "13": # Se a opção escolhida for 13
            relatorio_alunos_por_disciplina() # Chama a função para gerar um relatório de alunos por disciplina
        elif opcao == "14": # Se a opção escolhida for 14
            relatorio_detalhado_aluno() # Chama a função para gerar um relatório detalhado de um aluno específico
        elif opcao == "15": # Se a opção escolhida for 15
            verificar_conclusao_curso() # Chama a função para verificar se um aluno concluiu o curso
        elif opcao == "16": # Se a opção escolhida for 16
            verificar_conclusao_curso() # Chama a função para emitir um certificado de conclusão de curso    
        elif opcao == "0": # Se a opção escolhida for 0
            print("Saindo...") # Exibe mensagem de saída
            break # Encerra o loop e sai do programa
        else: # Se a opção escolhida não for válida
            print("Opção inválida!") # Exibe mensagem de opção inválida