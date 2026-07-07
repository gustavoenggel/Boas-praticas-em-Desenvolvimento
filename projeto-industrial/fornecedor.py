from database import conectar

def criar_Fornecedor():
    pass

def listar_fornecedor():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM fornecedor"
    cursor.execute(sql)
    dados = cursor.fetchall()

    for fornecedor in dados:
        print(fornecedor)

    cursor.close()
    conexao.close()

def deletar_fornecededor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM fornecedor WHERE id_fornecedor = %s"
    cursor.execute(sql, (id_fornecedor,))
    conexao.commit()

    print("Fornecedor removido com sucesso")

    cursor.close()
    conexao.close()

def atualizar_fornecedor():
    pass


