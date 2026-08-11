from database.conexao import Conexao
from models.fornecedor import Fornecedor


class FornecedorDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, fornecedor):
        """Recebe um objeto Fornecedor e o insere no banco PostgreSQL."""
        sql = """
              INSERT INTO empresa.fornecedor
              (razao_social, nome_fantasia, cnpj, inscricao_estadual, email,
               telefone, celular, site, cep, endereco, numero, complemento,
               bairro, cidade, estado, pais, nome_contato, cargo_contato,
               status, observacoes)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_fornecedor;
              """

        valores = (
            fornecedor.razao_social, fornecedor.nome_fantasia, fornecedor.cnpj,
            fornecedor.inscricao_estadual, fornecedor.email, fornecedor.telefone,
            fornecedor.celular, fornecedor.site, fornecedor.cep, fornecedor.endereco,
            fornecedor.numero, fornecedor.complemento, fornecedor.bairro,
            fornecedor.cidade, fornecedor.estado, fornecedor.pais,
            fornecedor.nome_contato, fornecedor.cargo_contato, fornecedor.status,
            fornecedor.observacoes
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            fornecedor.id_fornecedor = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Fornecedor {fornecedor.razao_social} inserido com ID {fornecedor.id_fornecedor}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir fornecedor: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os fornecedores e retorna uma lista de objetos Fornecedor."""
        sql = "SELECT * FROM empresa.fornecedor;"
        lista_fornecedores = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                fornec = Fornecedor(
                    id_fornecedor=linha[0], razao_social=linha[1], nome_fantasia=linha[2],
                    cnpj=linha[3], inscricao_estadual=linha[4], email=linha[5],
                    telefone=linha[6], celular=linha[7], site=linha[8], cep=linha[9],
                    endereco=linha[10], numero=linha[11], complemento=linha[12],
                    bairro=linha[13], cidade=linha[14], estado=linha[15], pais=linha[16],
                    nome_contato=linha[17], cargo_contato=linha[18], status=linha[19],
                    observacoes=linha[20]
                )
                lista_fornecedores.append(fornec)

            return lista_fornecedores

        except Exception as e:
            print(f"Erro ao buscar fornecedores: {e}")
            return []

    def buscarFornecedor(self, id_fornecedor):
        sql = """
              SELECT id_fornecedor, razao_social, nome_fantasia, cnpj, email, telefone, status
              FROM empresa.fornecedor \
              WHERE id_fornecedor = %s;
              """
        try:
            self.cursor.execute(sql, (id_fornecedor,))
            resultado = self.cursor.fetchone()

            if resultado:
                id_forn, razao, fantasia, cnpj, email, telefone, status = resultado

                # Trata campos vazios ou nulos para exibir '-'
                razao_str = razao.strip() if razao and razao.strip() else "-"
                fantasia_str = fantasia.strip() if fantasia and fantasia.strip() else "-"
                cnpj_str = cnpj.strip() if cnpj and cnpj.strip() else "-"
                email_str = email.strip() if email and email.strip() else "-"
                telefone_str = telefone.strip() if telefone and telefone.strip() else "-"
                status_str = status.strip() if status and status.strip() else "-"

                return (
                    f"\n========================================\n"
                    f"          DETALHES DO FORNECEDOR        \n"
                    f"========================================\n"
                    f" ID:            {id_forn}\n"
                    f" Razão Social:  {razao_str}\n"
                    f" Nome Fantasia: {fantasia_str}\n"
                    f" CNPJ:          {cnpj_str}\n"
                    f" E-mail:        {email_str}\n"
                    f" Telefone:      {telefone_str}\n"
                    f" Status:        {status_str}\n"
                    f"========================================"
                )
            return "Fornecedor não encontrado."
        except Exception as erro:
            print(f"Erro ao buscar fornecedor: {erro}")
            return None