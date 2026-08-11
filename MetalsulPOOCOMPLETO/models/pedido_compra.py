from database.conexao import Conexao


class PedidoCompra(Conexao):
    def __init__(self,
                 id_pedido_compra=None,
                 numero_pedido="",
                 data_pedido=None,
                 data_entrega_prevista=None,
                 status="PENDENTE",
                 valor_total=0.0,
                 valor_desconto=0.0,
                 forma_pagamento="",
                 observacoes="",
                 id_fornecedor=None,
                 id_funcionario=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_pedido_compra = id_pedido_compra
        self.numero_pedido = numero_pedido
        self.data_pedido = data_pedido
        self.data_entrega_prevista = data_entrega_prevista
        self.status = status
        self.valor_total = valor_total
        self.valor_desconto = valor_desconto
        self.forma_pagamento = forma_pagamento
        self.observacoes = observacoes
        self.id_fornecedor = id_fornecedor
        self.id_funcionario = id_funcionario