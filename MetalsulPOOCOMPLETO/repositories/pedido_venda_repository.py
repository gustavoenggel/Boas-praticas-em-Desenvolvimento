from database.conexao import Conexao
from models.pedido_venda import PedidoVenda


class PedidoVendaDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, pedido):
        sql = """
              INSERT INTO empresa.pedido_venda
              (numero_pedido, data_venda, valor_total, desconto,
               forma_pagamento, status, observacoes, id_cliente, id_funcionario)
              VALUES (%s, CURRENT_DATE, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_pedido_venda;
              """
        valores = (
            pedido.numero_pedido,
            pedido.valor_total,
            pedido.desconto,
            pedido.forma_pagamento,
            pedido.status,
            pedido.observacoes,
            pedido.id_cliente,
            pedido.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)
            pedido.id_pedido_venda = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Pedido de Venda '{pedido.numero_pedido}' inserido!")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir pedido de venda: {e}")
            return False

    def buscar_todos(self):
        sql = """
              SELECT id_pedido_venda, numero_pedido, data_venda, valor_total, 
                     desconto, forma_pagamento, status, observacoes, id_cliente, id_funcionario 
              FROM empresa.pedido_venda;
              """
        lista = []
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            for linha in registros:
                ped = PedidoVenda(
                    id_pedido_venda=linha[0],
                    numero_pedido=linha[1],
                    data_venda=linha[2],
                    valor_total=linha[3],
                    desconto=linha[4],
                    forma_pagamento=linha[5],
                    status=linha[6],
                    observacoes=linha[7],
                    id_cliente=linha[8],
                    id_funcionario=linha[9]
                )
                lista.append(ped)
            return lista
        except Exception as e:
            print(f"Erro ao buscar pedidos de venda: {e}")
            return []

    def buscarPedidoVenda(self, id_pedido_venda):
        sql = """
              SELECT id_pedido_venda, numero_pedido, data_venda, valor_total, 
                     desconto, forma_pagamento, status, observacoes, id_cliente, id_funcionario 
              FROM empresa.pedido_venda WHERE id_pedido_venda = %s;
              """
        try:
            self.cursor.execute(sql, (id_pedido_venda,))
            return self.cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar pedido de venda: {erro}")
            return None

    def ExcluirPedidoVenda(self, id_pedido_venda):
        sql = "DELETE FROM empresa.pedido_venda WHERE id_pedido_venda = %s;"
        try:
            self.cursor.execute(sql, (id_pedido_venda,))
            self.conexao.commit()
            print("Pedido de venda excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir pedido de venda: {erro}")