from database.conexao import Conexao
from models.cliente import Cliente


class ClienteDAO(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, cliente):
        """Insere um novo cliente no banco PostgreSQL e atualiza o objeto com o ID gerado."""
        sql = """
              INSERT INTO empresa.cliente
              (tipo_cliente, nome, cpf_cnpj, inscricao_estadual, email,
               telefone, celular, cep, endereco, numero, complemento,
               bairro, cidade, estado, pais, limite_credito, data_cadastro,
               status, observacoes)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING id_cliente;
              """

        valores = (
            cliente.tipo_cliente, cliente.nome, cliente.cpf_cnpj,
            cliente.inscricao_estadual, cliente.email, cliente.telefone,
            cliente.celular, cliente.cep, cliente.endereco, cliente.numero,
            cliente.complemento, cliente.bairro, cliente.cidade,
            cliente.estado, cliente.pais, cliente.limite_credito,
            cliente.data_cadastro, cliente.status, cliente.observacoes
        )

        try:
            self.cursor.execute(sql, valores)
            cliente.id_cliente = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"Sucesso: Cliente {cliente.nome} inserido com ID {cliente.id_cliente}")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir cliente: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os clientes e retorna uma lista de objetos Cliente."""
        sql = "SELECT * FROM empresa.cliente;"
        lista_clientes = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                cli = Cliente(
                    id_cliente=linha[0],
                    tipo_cliente=linha[1],
                    nome=linha[2],
                    cpf_cnpj=linha[3],
                    inscricao_estadual=linha[4],
                    email=linha[5],
                    telefone=linha[6],
                    celular=linha[7],
                    cep=linha[8],
                    endereco=linha[9],
                    numero=linha[10],
                    complemento=linha[11],
                    bairro=linha[12],
                    cidade=linha[13],
                    estado=linha[14],
                    pais=linha[15],
                    limite_credito=linha[16],
                    data_cadastro=linha[17],
                    status=linha[18],
                    observacoes=linha[19]
                )
                lista_clientes.append(cli)

            return lista_clientes
        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []

    def buscarCliente(self, id_cliente):
        """Busca um cliente pelo ID e retorna o registro encontrado."""
        sql = "SELECT * FROM empresa.cliente WHERE id_cliente = %s"
        try:
            self.cursor.execute(sql, (id_cliente,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar cliente! Erro: {erro}")
            return None

    def ExcluirCliente(self, id_cliente):
        """Exclui um cliente do banco de dados pelo ID."""
        sql = "DELETE FROM empresa.cliente WHERE id_cliente = %s"
        try:
            self.cursor.execute(sql, (id_cliente,))
            self.conexao.commit()
            print("Cliente excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir cliente! Erro: {erro}")

    def fechar(self):
        """Encerra a conexão herdada com o banco de dados."""
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")