CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS alunos (
    matricula TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    curso_id INTEGER,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_matricula TEXT NOT NULL,
    disciplina_codigo TEXT NOT NULL,
    FOREIGN KEY (aluno_matricula) REFERENCES alunos(matricula),
    FOREIGN KEY (disciplina_codigo) REFERENCES disciplinas(codigo)
);
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula_aluno TEXT NOT NULL,
    disciplina_codigo TEXT NOT NULL,
    nota REAL NOT NULL,
    FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula),
    FOREIGN KEY (disciplina_codigo) REFERENCES disciplinas(codigo)
);
CREATE TABLE IF NOT EXISTS professores (
    matricula TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    curso_id INTEGER,
    disciplina_codigo TEXT,
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (disciplina_codigo) REFERENCES disciplinas(codigo)
);