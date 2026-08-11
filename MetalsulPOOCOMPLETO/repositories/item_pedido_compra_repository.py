from database.conexao import Conexao
from models.item_pedido_compra import ItemPedidoCompra


class ItemPedidoCompraDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, item):
        """Recebe um objeto ItemPedidoCompra e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.item_pedido_compra
              (id_pedido_compra, id_produto, quantidade, preco_unitario, desconto, subtotal)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_item_pedido;
              """

        valores = (
            item.id_pedido_compra, item.id_produto, item.quantidade,
            item.preco_unitario, item.desconto, item.subtotal
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            item.id_item_pedido = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Item de Pedido inserido com ID {item.id_item_pedido}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir item de pedido de compra: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os itens de pedidos e retorna uma lista de objetos ItemPedidoCompra."""
        sql = "SELECT * FROM empresa.item_pedido_compra;"
        lista_itens = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                item = ItemPedidoCompra(
                    id_item_pedido=linha[0],
                    id_pedido_compra=linha[1],
                    id_produto=linha[2],
                    quantidade=linha[3],
                    preco_unitario=linha[4],
                    desconto=linha[5],
                    subtotal=linha[6]
                )
                lista_itens.append(item)

            return lista_itens

        except Exception as e:
            print(f"Erro ao buscar itens de pedido de compra: {e}")
            return []

    def buscarItemPedido(self, id_item_pedido):
        """Busca um único item de pedido pelo ID."""
        sql = "SELECT * FROM empresa.item_pedido_compra WHERE id_item_pedido = %s"
        try:
            self.cursor.execute(sql, (id_item_pedido,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar item de pedido de compra! Erro: {erro}")
            return None

    def ExcluirItemPedido(self, id_item_pedido):
        """Exclui um item de pedido pelo ID."""
        sql = "DELETE FROM empresa.item_pedido_compra WHERE id_item_pedido = %s"
        try:
            self.cursor.execute(sql, (id_item_pedido,))
            self.conexao.commit()
            print("Item de pedido de compra excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir item de pedido de compra! Erro: {erro}")

    def fechar(self):
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")