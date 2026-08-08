from database.conexao import Conexao
from models.produto import Produto


class ProdutoDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, produto):
        """Recebe um objeto Produto e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.produto
              (codigo, codigo_barras, descricao, unidade_medida, marca, modelo,
               fabricante, peso, altura, largura, comprimento, cor, preco_custo,
               preco_venda, margem_lucro, estoque_atual, estoque_minimo,
               estoque_maximo, localizacao, lote, data_fabricacao, data_validade,
               data_cadastro, ativo, id_categoria, id_fornecedor)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_produto;
              """

        valores = (
            produto.codigo, produto.codigo_barras, produto.descricao,
            produto.unidade_medida, produto.marca, produto.modelo,
            produto.fabricante, produto.peso, produto.altura, produto.largura,
            produto.comprimento, produto.cor, produto.preco_custo,
            produto.preco_venda, produto.margem_lucro, produto.estoque_atual,
            produto.estoque_minimo, produto.estoque_maximo, produto.localizacao,
            produto.lote, produto.data_fabricacao, produto.data_validade,
            produto.data_cadastro, produto.ativo, produto.id_categoria,
            produto.id_fornecedor
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            produto.id_produto = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Produto '{produto.descricao}' inserido com ID {produto.id_produto}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir produto: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os produtos e retorna uma lista de objetos Produto."""
        sql = "SELECT * FROM empresa.produto;"
        lista_produtos = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                prod = Produto(
                    id_produto=linha[0],
                    codigo=linha[1],
                    codigo_barras=linha[2],
                    descricao=linha[3],
                    unidade_medida=linha[4],
                    marca=linha[5],
                    modelo=linha[6],
                    fabricante=linha[7],
                    peso=linha[8],
                    altura=linha[9],
                    largura=linha[10],
                    comprimento=linha[11],
                    cor=linha[12],
                    preco_custo=linha[13],
                    preco_venda=linha[14],
                    margem_lucro=linha[15],
                    estoque_atual=linha[16],
                    estoque_minimo=linha[17],
                    estoque_maximo=linha[18],
                    localizacao=linha[19],
                    lote=linha[20],
                    data_fabricacao=linha[21],
                    data_validade=linha[22],
                    data_cadastro=linha[23],
                    ativo=linha[24],
                    id_categoria=linha[25],
                    id_fornecedor=linha[26]
                )
                lista_produtos.append(prod)

            return lista_produtos

        except Exception as e:
            print(f"Erro ao buscar produtos: {e}")
            return []

    def buscarProduto(self, id_produto):
        """Busca um único produto pelo ID."""
        sql = "SELECT * FROM empresa.produto WHERE id_produto = %s"
        try:
            self.cursor.execute(sql, (id_produto,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar produto! Erro: {erro}")
            return None

    def ExcluirProduto(self, id_produto):
        """Exclui um produto pelo ID."""
        sql = "DELETE FROM empresa.produto WHERE id_produto = %s"
        try:
            self.cursor.execute(sql, (id_produto,))
            self.conexao.commit()
            print("Produto excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir produto! Erro: {erro}")

    def fechar(self):
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")