from database.conexao import Conexao


class ItemPedidoCompra(Conexao):
    def __init__(self,
                 id_item_pedido=None,
                 id_pedido_compra=None,
                 id_produto=None,
                 quantidade=0,
                 preco_unitario=0.0,
                 desconto=0.0,
                 subtotal=0.0):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_item_pedido = id_item_pedido
        self.id_pedido_compra = id_pedido_compra
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.desconto = desconto
        self.subtotal = subtotal