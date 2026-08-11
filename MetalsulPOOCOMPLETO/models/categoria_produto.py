from database.conexao import Conexao


class CategoriaProduto(Conexao):
    def __init__(self,
                 id_categoria=None,
                 nome="",
                 descricao="",
                 ativo=True):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_categoria = id_categoria
        self.nome = nome
        self.descricao = descricao
        self.ativo = ativo