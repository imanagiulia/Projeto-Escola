from src.repository.alunos_repository import criar_aluno, ler_alunos, atualizar_aluno, deletar_aluno
from src.repository.professores_repository import criar_professor, ler_professores, atualizar_professor, deletar_professor
from src.repository.disciplina_repository import criar_disciplina, ler_disciplinas, atualizar_disciplina, deletar_disciplina
from src.repository.turmas_repository import criar_turma, ler_turmas, atualizar_turma, deletar_turma
from src.repository.notas_repository import criar_nota, ler_notas, atualizar_nota, deletar_nota
from src.repository.matricula_repository import matricular_aluno_turma, listar_alunos_turma, cancelar_matricula
from src.repository.grade_curricular_repository import alocar_disciplina, listar_grade_turma, remover_disciplina_grade

remover_disciplina_grade(7, 1)


