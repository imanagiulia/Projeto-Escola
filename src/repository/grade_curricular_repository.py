from src.database.connection import criar_conexao

def alocar_disciplina(id_turma, id_disciplina):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO turmas_disciplinas (id_turma, id_disciplina) VALUES (%s, %s)'

        cursor.execute(sql, (id_turma, id_disciplina))
        conexao.commit()
        print(f'Disciplina alocada com sucesso!')
    except Exception as e:
        print(f'Erro ao alocar disciplina: {e}')
    finally:
        cursor.close()
        conexao.close()

def listar_grade_turma(id_turma):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT d.nome_disciplina, t.nome_turma FROM turmas AS t JOIN turmas_disciplinas AS td ON t.id_turma = td.id_turma JOIN disciplinas AS d ON d.id_disciplina = td.id_disciplina WHERE td.id_turma = %s;'

        cursor.execute(sql, [id_turma])
        disciplinas_turma = cursor.fetchall()
        print(disciplinas_turma)
    except Exception as e:
        print(f'Erro ao listar a grade da turma:  {e}')
    finally:
        cursor.close()
        conexao.close()

def remover_disciplina_grade(id_disciplina, id_turma):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM turmas_disciplinas WHERE id_turma = %s AND id_disciplina = %s'

        cursor.execute(sql, (id_turma, id_disciplina))
        conexao.commit()
        print(f'Disciplina removida da grade da turma!')
    except Exception as e:
        print(f'Erro ao remover disciplina da grade da turma: {e}')
    finally:
        cursor.close()
        conexao.close()