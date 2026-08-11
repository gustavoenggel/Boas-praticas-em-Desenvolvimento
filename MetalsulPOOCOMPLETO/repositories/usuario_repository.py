from database.conexao import Conexao
from models.usuario import Usuario


class UsuarioDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, usuario):
        """Recebe um objeto Usuario e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.usuario
              (usuario, senha_hash, nivel_acesso, ultimo_login, ativo, id_funcionario)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_usuario;
              """

        valores = (
            usuario.usuario, usuario.senha_hash, usuario.nivel_acesso,
            usuario.ultimo_login, usuario.ativo, usuario.id_funcionario
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            usuario.id_usuario = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Usuário '{usuario.usuario}' inserido com ID {usuario.id_usuario}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir usuário: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os usuários e retorna uma lista de objetos Usuario."""
        sql = "SELECT * FROM empresa.usuario;"
        lista_usuarios = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                user = Usuario(
                    id_usuario=linha[0],
                    usuario=linha[1],
                    senha_hash=linha[2],
                    nivel_acesso=linha[3],
                    ultimo_login=linha[4],
                    ativo=linha[5],
                    id_funcionario=linha[6]
                )
                lista_usuarios.append(user)

            return lista_usuarios

        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []

    def buscarUsuario(self, id_usuario):
        """Busca um único usuário pelo ID."""
        sql = "SELECT * FROM empresa.usuario WHERE id_usuario = %s"
        try:
            self.cursor.execute(sql, (id_usuario,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar usuário! Erro: {erro}")
            return None

    def ExcluirUsuario(self, id_usuario):
        """Exclui um usuário pelo ID."""
        sql = "DELETE FROM empresa.usuario WHERE id_usuario = %s"
        try:
            self.cursor.execute(sql, (id_usuario,))
            self.conexao.commit()
            print("Usuário excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir usuário! Erro: {erro}")

    def fechar(self):
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")