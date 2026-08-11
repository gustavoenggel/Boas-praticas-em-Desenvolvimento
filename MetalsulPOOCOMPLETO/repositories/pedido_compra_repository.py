from database.conexao import Conexao
from models.pedido_compra import PedidoCompra


class PedidoCompraDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, pedido):
        """Recebe um objeto PedidoCompra e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.pedido_compra
              (numero_pedido, data_pedido, data_entrega_prevista, status,
               valor_total, valor_desconto, forma_pagamento, observacoes,
               id_fornecedor, id_funcionario)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_pedido_compra;
              """

        valores = (
            pedido.numero_pedido, pedido.data_pedido, pedido.data_entrega_prevista,
            pedido.status, pedido.valor_total, pedido.valor_desconto,
            pedido.forma_pagamento, pedido.observacoes, pedido.id_fornecedor,
            pedido.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            pedido.id_pedido_compra = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Pedido de Compra '{pedido.numero_pedido}' inserido com ID {pedido.id_pedido_compra}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir pedido de compra: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os pedidos de compra e retorna uma lista de objetos PedidoCompra."""
        sql = "SELECT * FROM empresa.pedido_compra;"
        lista_pedidos = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                ped = PedidoCompra(
                    id_pedido_compra=linha[0],
                    numero_pedido=linha[1],
                    data_pedido=linha[2],
                    data_entrega_prevista=linha[3],
                    status=linha[4],
                    valor_total=linha[5],
                    valor_desconto=linha[6],
                    forma_pagamento=linha[7],
                    observacoes=linha[8],
                    id_fornecedor=linha[9],
                    id_funcionario=linha[10]
                )
                lista_pedidos.append(ped)

            return lista_pedidos

        except Exception as e:
            print(f"Erro ao buscar pedidos de compra: {e}")
            return []

    def buscarPedidoCompra(self, id_pedido_compra):
        """Busca um único pedido de compra pelo ID."""
        sql = "SELECT * FROM empresa.pedido_compra WHERE id_pedido_compra = %s"
        try:
            self.cursor.execute(sql, (id_pedido_compra,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar pedido de compra! Erro: {erro}")
            return None

    def ExcluirPedidoCompra(self, id_pedido_compra):
        """Exclui um pedido de compra pelo ID."""
        sql = "DELETE FROM empresa.pedido_compra WHERE id_pedido_compra = %s"
        try:
            self.cursor.execute(sql, (id_pedido_compra,))
            self.conexao.commit()
            print("Pedido de compra excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir pedido de compra! Erro: {erro}")

    def fechar(self):
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")