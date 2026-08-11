from database.conexao import Conexao


class Produto(Conexao):
    def __init__(self,
                 id_produto=None,
                 codigo="",
                 codigo_barras="",
                 descricao="",
                 unidade_medida="UN",
                 marca="",
                 modelo="",
                 fabricante="",
                 peso=0.0,
                 altura=0.0,
                 largura=0.0,
                 comprimento=0.0,
                 cor="",
                 preco_custo=0.0,
                 preco_venda=0.0,
                 margem_lucro=0.0,
                 estoque_atual=0,
                 estoque_minimo=0,
                 estoque_maximo=0,
                 localizacao="",
                 lote="",
                 data_fabricacao=None,
                 data_validade=None,
                 data_cadastro="",
                 ativo=True,
                 id_categoria=None,
                 id_fornecedor=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_produto = id_produto
        self.codigo = codigo
        self.codigo_barras = codigo_barras
        self.descricao = descricao
        self.unidade_medida = unidade_medida
        self.marca = marca
        self.modelo = modelo
        self.fabricante = fabricante
        self.peso = peso
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.cor = cor
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.margem_lucro = margem_lucro
        self.estoque_atual = estoque_atual
        self.estoque_minimo = estoque_minimo
        self.estoque_maximo = estoque_maximo
        self.localizacao = localizacao
        self.lote = lote
        self.data_fabricacao = data_fabricacao
        self.data_validade = data_validade
        self.data_cadastro = data_cadastro
        self.ativo = ativo
        self.id_categoria = id_categoria
        self.id_fornecedor = id_fornecedor