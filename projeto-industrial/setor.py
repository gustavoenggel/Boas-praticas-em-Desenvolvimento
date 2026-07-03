from database import conectar

def listar_setores():
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Busca todos os setores cadastrados
    sql = """
    SELECT * FROM setor
    """
    
    cursor.execute(sql)
    setores = cursor.fetchall() # Busca todas as linhas do resultado
    
    print("\n--- Lista de Setores ---")
    if not setores:
        print("Nenhum setor cadastrado.")
    else:
        for setor in setores:
            # setor[0] é o id_setor e setor[1] é o nome
            print(f"ID: {setor[0]} | Nome: {setor[1]}")
    print("------------------------\n")
    
    cursor.close()
    conexao.close()
    
    return setores

def criar_setor(nome,localizacao):
    # 1. Corrigido: Adicionado os parênteses ()
    conn = conectar() 
    cursor = conn.cursor()

    # 2. Corrigido: Removido o 'SELECT' e ajustado para apenas um '%s'
    sql = """
    INSERT INTO setor(nome,localizacao)
    VALUES (%s,%s)
    """

    # 3. Corrigido: Adicionada a vírgula para transformar em uma tupla válida
    valores = (nome,localizacao) 
    
    cursor.execute(sql, valores)
    conn.commit()

    print('Setor criado com sucesso')
def atualizar_setor(id_setor,novo_nome,nova_localizacao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE setor
    SET nome = %s
        localizacao = %s
    WHERE id_setor = %s
    """
    valores = (nova_localizacao,novo_nome, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Setor atualizado com sucesso!")

    cursor.close()
    conexao.close()
    print( 'Setor atualizado')
def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from setor
    where id_setor= %s
    """
    valores = (id_setor)
    cursor.execute(sql, (valores,))
    conexao.commit()
    print("Funcionario removido com sucesso")

    cursor.close()
    conexao.close()
    print('Setor deletado')