from database.conexao import Conexao


class Fornecedor(Conexao):
    def __init__(self,
                 id_fornecedor=None,
                 razao_social="",
                 nome_fantasia="",
                 cnpj="",
                 inscricao_estadual="",
                 email="",
                 telefone="",
                 celular="",
                 site="",
                 cep="",
                 endereco="",
                 numero="",
                 complemento="",
                 bairro="",
                 cidade="",
                 estado="",
                 pais="Brasil",
                 nome_contato="",
                 cargo_contato="",
                 status="ATIVO",
                 observacoes=""):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_fornecedor = id_fornecedor
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.email = email
        self.telefone = telefone
        self.celular = celular
        self.site = site
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.nome_contato = nome_contato
        self.cargo_contato = cargo_contato
        self.status = status
        self.observacoes = observacoes