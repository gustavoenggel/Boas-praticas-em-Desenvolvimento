from database.conexao import Conexao


class Usuario(Conexao):
    def __init__(self,
                 id_usuario=None,
                 usuario="",
                 senha_hash="",
                 nivel_acesso="OPERADOR",
                 ultimo_login=None,
                 ativo=True,
                 id_funcionario=None):
        # Opcional: Se a classe pai (Conexao) precisar ser inicializada:
        # super().__init__()

        self.id_usuario = id_usuario
        self.usuario = usuario
        self.senha_hash = senha_hash
        self.nivel_acesso = nivel_acesso
        self.ultimo_login = ultimo_login
        self.ativo = ativo
        self.id_funcionario = id_funcionario