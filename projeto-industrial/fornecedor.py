from database import conectar

def deletar_fornecededor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from fornecedor
    where id_fornecedor = %s
    """
    valores = (id_fornecedor)
    cursor.execute(sql, (valores,))
    conexao.commit()
    print("Fornecedor removido com sucesso")

    cursor.close()
    conexao.close()