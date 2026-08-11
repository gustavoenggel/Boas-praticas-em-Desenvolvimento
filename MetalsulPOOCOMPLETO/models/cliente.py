from database.conexao import Conexao
from datetime import date

class Cliente(Conexao):
    def __init__(self,
                 id_cliente=None,
                 tipo_cliente="PF",
                 nome="",
                 cpf_cnpj="",
                 inscricao_estadual="",
                 email="",
                 telefone="",
                 celular="",
                 cep="",
                 endereco="",
                 numero="",
                 complemento="",
                 bairro="",
                 cidade="",
                 estado="",
                 pais="Brasil",
                 limite_credito=0.0,
                 data_cadastro=date.today(),
                 status="ATIVO",
                 observacoes=""):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        super().__init__()

        self.id_cliente = id_cliente
        self.tipo_cliente = tipo_cliente
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.inscricao_estadual = inscricao_estadual
        self.email = email
        self.telefone = telefone
        self.celular = celular
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.limite_credito = limite_credito
        self.data_cadastro = data_cadastro
        self.status = status
        self.observacoes = observacoes