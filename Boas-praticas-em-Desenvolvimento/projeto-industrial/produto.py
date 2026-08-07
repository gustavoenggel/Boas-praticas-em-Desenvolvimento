from database import conectar

def criar_PRODUTO(): #LIA
    pass
def listar_PRODUTO():#
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT 
                p.id_produto,
                p.nome,
                p.preco_fabricacao,
                p.quantidade_estoque,
                c.nome as categoria,
                f.razao_social as fornecedor
            FROM produto p
            JOIN categoria_produto as c 
                on p.id_categoria = c.id_categoria
            JOIN fornecedor as f
                on f.id_fornecedor = p.id_fornecedor
            """
        #executa sql
        cursor.execute(sql)
        #recuperar dados
        produtos = cursor.fetchall()
        #exibir dados
        for produto in produtos:
            print(f"\nID:{produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Preco fabricacao: R${produto[2]}")
            print(f"Estoque: {produto[3]}")
            print(f"Categoria: {produto[4]}")
            print(f"Fornecedor: {produto[5]}")
            print("-"*40)


        #fechar a conexao

        cursor.close()
        conexao.close()

    except Exception as erro:
            print(erro)
        

    pass
def deletar_PRODUTO():#GABRIEL
    pass
def atualizar_PRODUTO():#AUGUSTO
    pass
def buscar_produto(): #arthur
    pass

