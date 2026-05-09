from src.database.connection import criar_conexao

def criar_aluno(nome, nascimento, genero, endereco, telefone, email):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'INSERT INTO alunos (nome_aluno, data_nascimento, genero, endereco, telefone_contato, email) VALUES (%s, %s, %s, %s, %s, %s)'

        cursor.execute(sql, (nome, nascimento, genero, endereco, telefone, email))
        conexao.commit()
        print("Aluno criado com sucesso!")
    except Exception as e:
        print(f'Erro ao criar aluno: {e}')
    finally:
        cursor.close()
        conexao.close()

def ler_alunos():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'SELECT * FROM alunos'

        cursor.execute(sql)
        alunos = cursor.fetchall()
        print(alunos)
    except Exception as e:
        print(f'Erro ao retornar tabela alunos: {e}')
    finally:
        cursor.close()
        conexao.close()

def atualizar_aluno(coluna, valor, id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = f'UPDATE alunos SET {coluna} = %s WHERE id_aluno = %s'

        cursor.execute(sql, (valor, id))
        conexao.commit()
        print(f'Aluno id:{id} atualizado com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar aluno: {e}')
    finally:
        cursor.close()
        conexao.close()

def deletar_aluno(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        sql = 'DELETE FROM alunos WHERE id_aluno = %s'

        cursor.execute(sql, [id])
        conexao.commit()
        print(f'Aluno id:{id} excluído com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir aluno: {e}')
    finally:
        cursor.close()
        conexao.close()
