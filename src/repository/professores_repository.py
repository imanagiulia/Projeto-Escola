from src.database.connection import criar_conexao

def criar_professor(nome, nascimento, genero, telefone, email):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO professores (nome_professor, data_nascimento, genero, telefone_contato, email) VALUES (%s, %s, %s, %s, %s)'

        cursor.execute(sql, (nome, nascimento, genero, telefone, email))
        conexao.commit()
        print(f'Professor cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar professor: {e}')
    finally:
        cursor.close()
        conexao.close()

def ler_professores():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT * FROM professores'

        cursor.execute(sql)
        professores = cursor.fetchall()
        print(professores)
    except Exception as e:
        print(f'Erro ao retornar tabela professores: {e}')
    finally:
        cursor.close()
        conexao.close()

def atualizar_professor(coluna, valor, id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = f'UPDATE professores SET {coluna} = %s WHERE id_professor = %s'

        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f'Professor id:{id} atualizado com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar professor: {e}')
    finally:
        cursor.close()
        conexao.close()
    
def deletar_professor(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM professores WHERE id_professor = %s'

        cursor.execute(sql, [id])
        conexao.commit()
        print('Professor excluído com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir professor: {e}')