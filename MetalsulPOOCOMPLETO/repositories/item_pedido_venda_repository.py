from database.conexao import Conexao
from models.item_pedido_venda import ItemPedidoVenda


class ItemPedidoVendaDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, item):
        sql = """
              INSERT INTO empresa.item_pedido_venda
              (id_pedido_venda, id_produto, quantidade, preco_unitario, desconto, subtotal)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_item_venda;
              """
        valores = (
            item.id_pedido_venda,
            item.id_produto,
            item.quantidade,
            item.preco_unitario,
            item.desconto,
            item.subtotal
        )

        try:
            self.cursor.execute(sql, valores)
            item.id_item_venda = self.cursor.fetchone()[0]
            self.conexao.commit()
            print("Sucesso: Item do pedido de venda inserido!")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir item do pedido de venda: {e}")
            return False

    def buscar_todos(self):
        sql = """
              SELECT id_item_venda, id_pedido_venda, id_produto, quantidade, 
                     preco_unitario, desconto, subtotal 
              FROM empresa.item_pedido_venda;
              """
        lista = []
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            for linha in registros:
                item = ItemPedidoVenda(
                    id_item_venda=linha[0],
                    id_pedido_venda=linha[1],
                    id_produto=linha[2],
                    quantidade=linha[3],
                    preco_unitario=linha[4],
                    desconto=linha[5],
                    subtotal=linha[6]
                )
                lista.append(item)
            return lista
        except Exception as e:
            print(f"Erro ao buscar itens do pedido de venda: {e}")
            return []

    def buscarItemVenda(self, id_item_venda):
        sql = """
              SELECT id_item_venda, id_pedido_venda, id_produto, quantidade, 
                     preco_unitario, desconto, subtotal 
              FROM empresa.item_pedido_venda WHERE id_item_venda = %s;
              """
        try:
            self.cursor.execute(sql, (id_item_venda,))
            return self.cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar item do pedido de venda: {erro}")
            return None

    def ExcluirItemVenda(self, id_item_venda):
        sql = "DELETE FROM empresa.item_pedido_venda WHERE id_item_venda = %s;"
        try:
            self.cursor.execute(sql, (id_item_venda,))
            self.conexao.commit()
            print("Item do pedido de venda excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir item do pedido de venda: {erro}")