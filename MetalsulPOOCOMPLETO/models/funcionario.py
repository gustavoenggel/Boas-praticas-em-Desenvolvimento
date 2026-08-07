#from database.conexao import Conexao

from datetime import date 

#classe funcionario
class Funcionario:
    def __init__(self,id_funcionario = None,
                 nome = "",
                 cpf = "",
                rg = "",
                data_nascimento = None,
                sexo = "",
                estado_civil = "",
                telefone = "",
                celular = "",
                cargo = "",
                departamento = "",
                salario = 0.0,
                data_admissao = "",
                turno = "",
                status = "ATIVO",
                observacoes = ""
                ):
        
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.celular = celular
        self.cargo = cargo
        self.departamento = departamento
        self.salario = salario
        self.data_admissao = data_admissao
        self.turno = turno
        self.status = status
        self.observacoes = observacoes


    def __str__(self):
        return (
            f"=== DADOS FUNCIONÁRIO ===\n"
            f"Funcionário: {self.nome}\n"
            f"CPF do funcionário: {self.cpf}\n"
            f"Cargo do funcionário: {self.cargo}\n"
            f"Departamento do funcionário: {self.departamento}\n"
            f"Salário do funcionário: {self.salario}\n"
            f"Status: {self.status}\n"
            f"{'='*30}"
        )
