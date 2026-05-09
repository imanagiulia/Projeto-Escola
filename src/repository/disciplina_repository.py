from src.database.connection import criar_conexao

def criar_disciplina(nome, descricao, ch, id_professor):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO disciplinas (nome_disciplina, descricao, carga_horaria, id_professor) VALUES (%s, %s, %s, %s)'

        cursor.execute(sql, (nome, descricao, ch, id_professor))
        conexao.commit()
        print(f'Disciplina cadastrada com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar disciplina: {e}')
    finally:
        cursor.close()
        conexao.close()

def ler_disciplinas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT * FROM disciplinas'

        cursor.execute(sql)
        disciplinas = cursor.fetchall()
        print(disciplinas)
    except Exception as e:
        print(f'Erro ao retornar tabela disciplinas: {e}')
    finally:
        cursor.close()
        conexao.close()

def atualizar_disciplina(coluna, valor, id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = f'UPDATE disciplinas SET {coluna} = %s WHERE id_disciplina = %s'

        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f'Disciplina id:{id} atualizada com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar disciplina: {e}')
    finally:
        cursor.close()
        conexao.close()

def deletar_disciplina(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM disciplinas WHERE id_disciplina = %s'

        cursor.execute(sql, [id])
        conexao.commit()
        print(f'Disciplina excluída com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir disciplina: {e}')
    finally:
        cursor.close()
        conexao.close()