from src.database.connection import criar_conexao

def criar_turma(nome,ano, id_professor):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO turmas (nome_turma, ano_letivo, id_professor_orientador) VALUES (%s, %s, %s)'

        cursor.execute(sql, (nome, ano, id_professor))
        conexao.commit()
        print(f'Turma cadastrada com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar turma: {e}')
    finally:
        cursor.close()
        conexao.close()

def ler_turmas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT * FROM turmas'

        cursor.execute(sql)
        turmas = cursor.fetchall()
        print(turmas)
    except Exception as e:
        print(f'Erro ao retornar tabela turmas: {e}')
    finally:
        cursor.close()
        conexao.close()

def atualizar_turma(coluna, valor, id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = f'UPDATE turmas SET {coluna} = %s WHERE id_turma = %s'

        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f'Turma id:{id} atualizada com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar turma: {e}')
    finally:
        cursor.close()
        conexao.close()

def deletar_turma(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM turmas WHERE id_turma = %s'

        cursor.execute(sql, [id])
        conexao.commit()
        print(f'Turma excluída com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir turma: {e}')
    finally:
        cursor.close()
        conexao.close()