from database.conexao import Conexao
from models.funcionario import Funcionario


class FuncionarioRepository(Conexao):
    def __init__(self):
        super().__init__()

    def inserir(self, funcionario):
        sql = """
              INSERT INTO empresa.funcionario
              (nome, cpf, cargo, departamento, salario, data_admissao)
              VALUES (%s, %s, %s, %s, %s, %s)
              RETURNING id_funcionario;
              """
        data_adm = getattr(funcionario, 'data_admissao', None) or '2026-08-11'
        valores = (
            funcionario.nome,
            funcionario.cpf,
            funcionario.cargo,
            funcionario.departamento,
            funcionario.salario,
            data_adm
        )

        try:
            self.cursor.execute(sql, valores)
            funcionario.id_funcionario = self.cursor.fetchone()[0]
            self.conexao.commit()
            print(f"\nSucesso: Funcionário '{funcionario.nome}' inserido com sucesso!")
            return True
        except Exception as e:
            self.conexao.rollback()
            print(f"\nErro ao inserir funcionário: {e}")
            return False

    def buscar_todos(self):
        sql = """
              SELECT id_funcionario, nome, cpf, cargo, departamento, salario 
              FROM empresa.funcionario;
              """
        lista = []
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            for linha in registros:
                f = Funcionario(
                    nome=linha[1],
                    cpf=linha[2],
                    cargo=linha[3],
                    departamento=linha[4],
                    salario=linha[5]
                )
                f.id_funcionario = linha[0]
                lista.append(f)
            return lista
        except Exception as e:
            print(f"Erro ao buscar funcionários: {e}")
            return []

    def buscarFuncionario(self, id_funcionario):
        sql = """
              SELECT id_funcionario, nome, cpf, cargo, departamento, salario 
              FROM empresa.funcionario WHERE id_funcionario = %s;
              """
        try:
            self.cursor.execute(sql, (id_funcionario,))
            resultado = self.cursor.fetchone()

            if resultado:
                id_func, nome, cpf, cargo, depto, salario = resultado
                salario_fmt = f"R$ {salario:.2f}" if salario is not None else "R$ 0.00"

                return (
                    f"\n========================================\n"
                    f"         DETALHES DO FUNCIONÁRIO        \n"
                    f"========================================\n"
                    f" ID:           {id_func}\n"
                    f" Nome:         {nome}\n"
                    f" CPF:          {cpf}\n"
                    f" Cargo:        {cargo}\n"
                    f" Departamento: {depto}\n"
                    f" Salário:      {salario_fmt}\n"
                    f"========================================"
                )
            return "Funcionário não encontrado."
        except Exception as erro:
            print(f"Erro ao buscar funcionário: {erro}")
            return None