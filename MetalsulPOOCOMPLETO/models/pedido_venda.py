from database.conexao import Conexao


class PedidoVenda(Conexao):
    def __init__(self,
                 id_pedido_venda=None,
                 numero_pedido="",
                 data_venda=None,
                 valor_total=0.0,
                 desconto=0.0,
                 forma_pagamento="",
                 status="ABERTO",
                 observacoes="",
                 id_cliente=None,
                 id_funcionario=None):
        self.id_pedido_venda = id_pedido_venda
        self.numero_pedido = numero_pedido
        self.data_venda = data_venda
        self.valor_total = valor_total
        self.desconto = desconto
        self.forma_pagamento = forma_pagamento
        self.status = status
        self.observacoes = observacoes
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario