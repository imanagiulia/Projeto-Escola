INSERT into alunos (
	nome_aluno, data_nascimento, genero, endereco, telefone_contato, email
)
VALUES 
('João Silva','2005-03-15','Masculino','Rua das Flores, 123','(11) 9876-5432','joao@email.com'),
('Maria Santos','2006-06-20','Feminino','Avenida Principal, 456','(11) 8765-4321','maria@email.com'),
('Pedro Soares','2004-01-10','Masculino','Rua Central, 789','(11) 7654-3210','pedro@email.com'),
('Ana Lima','2005-04-02','Feminino','Rua da Escola, 56','(11) 8765-4321','ana@email.com'),
('Mariana Fernandes','2005-08-12','Feminino','Avenida da Paz, 789','(11) 5678-1234','mariana@email.com'),
('Lucas Costa','2003-11-25','Masculino','Rua Principal, 456','(11) 1234-5678','lucas@email.com'),
('Isabela Santos','2006-09-10','Feminino','Rua da Amizade, 789','(11) 9876-5432','isabela@email.com'),
('Gustavo Pereira','2004-05-15','Masculino','Avenida dos Sonhos, 123','(11) 7654-3210','gustavo@email.com'),
('Carolina Oliveira','2005-02-20','Feminino','Rua da Alegria, 456','(11) 8765-4321','carolina@email.com'),
('Daniel Silva','2003-10-05','Masculino','Avenida Central, 789','(11) 1234-5678','daniel@email.com'),
('Larissa Souza','2004-12-08','Feminino','Rua da Felicidade, 123','(11) 9876-5432','larissa@email.com'),
('Bruno Costa','2005-07-30','Masculino','Avenida Principal, 456','(11) 7654-3210','bruno@email.com'),
('Camila Rodrigues','2006-03-22','Feminino','Rua das Estrelas, 789','(11) 8765-4321','camila@email.com'),
('Rafael Fernandes','2004-11-18','Masculino','Avenida dos Sonhos, 123','(11) 1234-5678','rafael@email.com'),
('Letícia Oliveira','2005-01-05','Feminino','Rua da Alegria, 456','(11) 9876-5432','leticia@email.com'),
('Fernanda Lima','2004-02-12','Feminino','Rua da Esperança, 789','(11) 4567-8901','fernanda@email.com'),
('Vinícius Santos','2003-07-28','Masculino','Avenida da Amizade, 123','(11) 8901-2345','vinicius@email.com'),
('Juliana Pereira','2006-09-01','Feminino','Rua das Rosas, 789','(11) 3456-7890','juliana@email.com');


INSERT into disciplinas (
  nome_disciplina, descricao, carga_horaria, id_professor
)
VALUES 
('Matemática','Estudo de conceitos matemáticos avançados','60','1'),
('História','História mundial e local','45', '2'),
('Física','Princípios fundamentais da física','60','1'),
('Química','Estudo da química e suas aplicações','45','3'),
('Inglês','Aulas de inglês para iniciantes','45','4'),
('Artes','Exploração da criatividade artística','30','5');

INSERT into notas (
  id_aluno, id_disciplina, valor_nota, data_avaliacao
 )
 VALUES
('1','1','6.1','07/07/2023'),
('1','2','7.1','07/07/2023'),
('1','3','7.4','07/07/2023'),
('1','4','7.4','07/07/2023'),
('1','5','4.3','07/07/2023'),
('1','6','4.4','07/07/2023'),
('1','7','0.7','07/07/2023'),
('1','8','9.2','07/07/2023'),
('1','9','9.0','07/07/2023'),
('1','10','3.8','07/07/2023'),
('2','1','1.3','09/07/2023'),
('2','2','3.1','09/07/2023'),
('2','3','1.6','09/07/2023'),
('2','4','0.3','09/07/2023'),
('2','5','4.4','09/07/2023'),
('2','6','4.2','09/07/2023'),
('2','7','8.9','09/07/2023'),
('2','8','1.7','09/07/2023'),
('2','9','8.6','09/07/2023'),
('2','10','3.1','09/07/2023'),
('3','1','6.2','27/07/2023'),
('3','2','8.1','27/07/2023'),
('3','3','1.3','27/07/2023'),
('3','4','4.1','27/07/2023'),
('3','5','0.5','27/07/2023'),
('3','6','6.3','27/07/2023'),
('3','7','9.4','27/07/2023'),
('3','8','3.7','27/07/2023'),
('3','9','0.8','27/07/2023'),
('3','10','8.2','27/07/2023'),
('4','1','8.7','08/08/2023'),
('4','2','0.6','08/08/2023'),
('4','3','5.5','08/08/2023'),
('4','4','6.8','08/08/2023'),
('4','5','6.8','08/08/2023'),
('4','6','4.9','08/08/2023'),
('4','7','7.6','08/08/2023'),
('4','8','0.2','08/08/2023'),
('4','9','7.7','08/08/2023'),
('4','10','5.81','08/08/2023'),
('5','1','2.25','15/08/2023'),
('5','2','5.82','15/08/2023'),
('5','3','4.11','15/08/2023'),
('5','4','7.99','15/08/2023'),
('5','5','3.23','15/08/2023'),
('5','6','8.09','15/08/2023'),
('5','7','8.24','15/08/2023'),
('5','8','3.33','15/08/2023'),
('5','9','4.24','15/08/2023'),
('5','10','0.11','15/08/2023');


INSERT into professores (
  nome_professor, data_nascimento, genero, telefone_contato, email
)
VALUES
('Ana Oliveira', '1980-05-25', 'Feminino', '(11) 1234-5678', 'ana@email.com'),
('Carlos Ferreira', '1975-09-12', 'Masculino', '(11) 2345-6789', 'carlos@email.com'),
('Mariana Santos', '1982-03-15', 'Feminino', '(11) 3456-7890', 'mariana@email.com'),
('Ricardo Silva', '1978-08-20', 'Masculino', '(11) 7890-1234', 'ricardo@email.com'),
('Fernanda Lima', '1985-01-30', 'Feminino', '(11) 4567-8901', 'fernanda@email.com');

INSERT into turmas (
  nome_turma, ano_letivo, id_professor_orientador
)
VALUES
('Turma A', '2023', '1'),
('Turma B', '2023', '2'),
('Turma C', '2023', '3'),
('Turma D', '2023', '4'),
('Turma E', '2023', '5');

INSERT into turma_alunos (
  id_aluno, id_turma
)
VALUES
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('1', '6'),
('2', '7'),
('3', '8'),
('4', '9'),
('5', '10');

INSERT into turmas_disciplinas (
  id_turma, id_disciplina
)
VALUES
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('1', '3'),
('2', '1'),
('3', '2');
