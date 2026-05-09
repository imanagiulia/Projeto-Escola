from src.database.connection import criar_conexao

def matricular_aluno_turma(id_aluno, id_turma):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO turma_alunos (id_aluno, id_turma) VALUES (%s, %s)'

        cursor.execute(sql, (id_aluno, id_turma))
        conexao.commit()
        print(f'Matrícula realizada com sucesso!')
    except Exception as e:
        print(f'Erro ao matricular aluno: {e}')
    finally:
        cursor.close()
        conexao.close()

def listar_alunos_turma(id_turma):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT DISTINCT a.nome_aluno, t.nome_turma, t.id_turma FROM alunos AS a JOIN turma_alunos AS ta ON ta.id_aluno = a.id_aluno JOIN turmas AS t ON t.id_turma = ta.id_turma WHERE t.id_turma = %s'

        cursor.execute(sql, [id_turma])
        alunos_turma = cursor.fetchall()
        print(alunos_turma)
    except Exception as e:
        print(f'Erro ao retornar lista de alunos matriculados na turma de id = {id_turma}: {e}')
    finally:
        cursor.close()
        conexao.close()

def cancelar_matricula(id_aluno, id_turma):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM turma_alunos WHERE id_aluno = %s AND id_turma = %s'

        cursor.execute(sql, (id_aluno, id_turma))
        conexao.commit()
        print('Matrícula cancelada com sucesso!')
    except Exception as e:
        print(f'Erro ao cancelar matrícula: {e}')
    finally:
        cursor.close()
        conexao.close()