from database.conexao import Conexao
from models.categoria_produto import CategoriaProduto


class CategoriaProdutoDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, categoria):
        """Recebe um objeto CategoriaProduto e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.categoria_produto
              (nome, descricao, ativo)
              VALUES (%s, %s, %s)
              RETURNING id_categoria;
              """

        valores = (
            categoria.nome, categoria.descricao, categoria.ativo
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            categoria.id_categoria = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Categoria '{categoria.nome}' inserida com ID {categoria.id_categoria}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir categoria: {e}")
            return False

    def buscar_todos(self):
        """Busca todas as categorias e retorna uma lista de objetos CategoriaProduto."""
        sql = "SELECT * FROM empresa.categoria_produto;"
        lista_categorias = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                cat = CategoriaProduto(
                    id_categoria=linha[0],
                    nome=linha[1],
                    descricao=linha[2],
                    ativo=linha[3]
                )
                lista_categorias.append(cat)

            return lista_categorias

        except Exception as e:
            print(f"Erro ao buscar categorias: {e}")
            return []

    def buscarCategoria(self, id_categoria):
        """Busca uma única categoria pelo ID."""
        sql = "SELECT * FROM empresa.categoria_produto WHERE id_categoria = %s"
        try:
            self.cursor.execute(sql, (id_categoria,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar categoria! Erro: {erro}")
            return None

    def ExcluirCategoria(self, id_categoria):
        """Exclui uma categoria pelo ID."""
        sql = "DELETE FROM empresa.categoria_produto WHERE id_categoria = %s"
        try:
            self.cursor.execute(sql, (id_categoria,))
            self.conexao.commit()
            print("Categoria excluída com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir categoria! Erro: {erro}")

    def fechar(self):
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")