create table alunos (
  id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_aluno VARCHAR(250),
  data_nascimento DATE,
  genero VARCHAR(100),
  endereco VARCHAR(250),
  telefone_contato VARCHAR(13),
  email VARCHAR(100)
);

create table professores (
  id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_professor VARCHAR(250),
  data_nascimento DATE,
  genero VARCHAR(100),
  telefone_contato VARCHAR(13),
  email VARCHAR(100)
);
 
create TABLE disciplinas (
  id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_disciplina VARCHAR(100),
  descricao VARCHAR(250),
  carga_horaria INT,
  id_professor INT,
  FOREIGN KEY (id_professor) REFERENCES professores(id_professor) on DELETE CASCADE
);

create table turmas (
  id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_turma VARCHAR(100),
  ano_letivo INT,
  id_professor_orientador INT,
  FOREIGN key (id_professor_orientador) REFERENCES professores(id_professor) on DELETE CASCADE
);

CREATE table turmas_disciplinas (
  id_turma INT,
  id_disciplina INT,
  FOREIGN KEY (id_turma) REFERENCES turmas(id_turma) on DELETE CASCADE,
  FOREIGN key (id_disciplina) REFERENCES disciplinas(id_disciplina) on DELETE CASCADE
);

CREATE table turma_alunos (
  id_aluno INT,
  id_turma INT,
  FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno) ON DELETE CASCADE,
  FOREIGN KEY (id_turma) REFERENCES turmas(id_turma) on DELETE CASCADE
);

CREATE table notas (
  id_nota INTEGER PRIMARY key AUTOINCREMENT,
  id_aluno INT,
  id_disciplina INT,
  valor_nota DECIMAL(2,1),
  data_avaliacao DATE,
  FOREIGN key (id_aluno) REFERENCES alunos(id_aluno),
  FOREIGN key (id_disciplina) REFERENCES disciplinas(id_disciplina)
);
