from database.conexao import Conexao
from models.funcionario import Funcionario


class FuncionarioDAO(Conexao):
    def __init__(self):
        # Inicializa a conexão com o banco herdada da classe Conexao
        super().__init__()

    def inserir(self, funcionario):
        """Recebe um objeto Funcionario e o insere no banco PostgreSQL."""

        # CORREÇÃO 1: Tabela alterada para 'empresa.funcionario'
        # CORREÇÃO 2: Adicionado 'RETURNING id_funcionario' no final para o fetchone() funcionar
        sql = """
              INSERT INTO empresa.funcionario
              (nome, cpf, rg, data_nascimento, sexo, estado_civil, email,
               telefone, celular, cargo, departamento, salario, data_admissao,
               data_demissao, turno, status, observacoes)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_funcionario;
              """

        valores = (
            funcionario.nome, funcionario.cpf, funcionario.rg, funcionario.data_nascimento,
            funcionario.sexo, funcionario.estado_civil, funcionario.email,
            funcionario.telefone, funcionario.celular, funcionario.cargo,
            funcionario.departamento, funcionario.salario, funcionario.data_admissao,
            funcionario.data_demissao, funcionario.turno, funcionario.status,
            funcionario.observacoes
        )

        try:
            self.cursor.execute(sql, valores)

            # Atualiza o ID do objeto com o ID gerado pelo banco
            funcionario.id_funcionario = self.cursor.fetchone()[0]
            self.conexao.commit()

            print(f"Sucesso: Funcionário {funcionario.nome} inserido com ID {funcionario.id_funcionario}")
            return True

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao inserir funcionário: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os funcionários e retorna uma lista de objetos Funcionario."""

        # CORREÇÃO 1: Tabela alterada para 'empresa.funcionario'
        sql = "SELECT * FROM empresa.funcionario;"
        lista_funcionarios = []

        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()

            for linha in registros:
                # Mapeia as colunas do banco para o objeto Python
                func = Funcionario(
                    id_funcionario=linha[0], nome=linha[1], cpf=linha[2], rg=linha[3],
                    data_nascimento=linha[4], sexo=linha[5], estado_civil=linha[6],
                    email=linha[7], telefone=linha[8], celular=linha[9], cargo=linha[10],
                    departamento=linha[11], salario=linha[12], data_admissao=linha[13],
                    data_demissao=linha[14], turno=linha[15], status=linha[16], observacoes=linha[17]
                )
                lista_funcionarios.append(func)

            return lista_funcionarios

        except Exception as e:
            print(f"Erro ao buscar funcionários: {e}")
            return []

    def buscarFuncionario(self, id_funcionario):
        sql = "SELECT * FROM empresa.funcionario WHERE id_funcionario = %s"
        try:
            self.cursor.execute(sql, (id_funcionario,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f"Erro ao buscar funcionário! Erro: {erro}")
            return None

    def ExcluirFuncionario(self, id_funcionario):
        sql = "DELETE FROM empresa.funcionario WHERE id_funcionario = %s"
        try:
            self.cursor.execute(sql, (id_funcionario,))
            self.conexao.commit()
            print("Funcionário excluído com sucesso!")
        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro ao excluir funcionário! Erro: {erro}")

    def fechar(self):
        # Assumindo que a classe Conexao tem um método fechar()
        try:
            super().fechar()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")