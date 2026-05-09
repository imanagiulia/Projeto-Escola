from src.database.connection import criar_conexao

def criar_nota(id_aluno, id_disciplina, valor_nota, data):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO notas (id_aluno, id_disciplina, valor_nota, data_avaliacao) VALUES (%s, %s, %s, %s)'

        cursor.execute(sql, (id_aluno, id_disciplina, valor_nota, data))
        conexao.commit()
        print(f'Nota cadastrada com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar nota: {e}')
    finally:
        cursor.close()
        conexao.close()

def ler_notas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT * FROM notas'

        cursor.execute(sql)
        notas = cursor.fetchall()
        print(notas)
    except Exception as e:
        print(f'Erro ao retornar tabela notas: {e}')
    finally:
        cursor.close()
        conexao.close()

def atualizar_nota(coluna, valor, id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = f'UPDATE notas SET {coluna} = %s WHERE id_nota = %s'

        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f'Nota id:{id} atualizada com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar nota: {e}')
    finally:
        cursor.close()
        conexao.close()

def deletar_nota(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM notas WHERE id_nota = %s'

        cursor.execute(sql, [id])
        conexao.commit()
        print(f'Nota excluída com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir nota: {e}')
    finally:
        cursor.close()
        conexao.close()