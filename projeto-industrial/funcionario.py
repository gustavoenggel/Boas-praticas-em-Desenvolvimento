#AGORA ESSE ARQUIVO É UM MÓDULO
#RESPONSÁVEL POR FUNCIONALIDADES REFERENTES A FUNCIONÁRIO

#listar conexão
from database import conectar


def listar_funcionarios():
#Abrir conexão
    conexao = conectar()

    #Criar cursor

    cursor = conexao.cursor()

    #sql da consulta

    sql = """
    SELECT 
        f.id_funcionario, 
        f.nome, 
        f.cargo, 
        s.nome AS setor,
        f.cpf,
        f.salario,
        f.data_admissao
    FROM funcionario f
    JOIN setor s ON f.id_setor = s.id_setor
    """
    
    # executa sql
    cursor.execute(sql)
    
    # recuperar dados
    dados = cursor.fetchall()
    
    # exibir dados
    for funcionario in dados:
        print(funcionario)
        
    # fechar a conexão
    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome,cargo,id_setor,cpf,salario,data_admissao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO funcionario (nome, cargo, id_setor,cpf,salario,data_admissao)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cargo, id_setor,cpf,salario,data_admissao)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Funcionário cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_cargo(id_funcionario, novo_cargo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE funcionario
    SET cargo = %s
    WHERE id_funcionario = %s
    """
    valores = (novo_cargo, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Cargo do funcionário atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from funcionario
    where id_funcionario = %s
    """
    valores = (id_funcionario)
    cursor.execute(sql, (valores,))
    conexao.commit()
    print("Funcionario removido com sucesso")

    cursor.close()
    conexao.close()

