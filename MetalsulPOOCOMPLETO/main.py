#from database.conexao import Conexao
from datetime import date
from models import funcionario
from models.funcionario import Funcionario

def main():
    funcionario = Funcionario(nome = "Maria garcia",
                            cpf = "6969696969",
                            cargo = "Chao de fabrica",
                            departamento = "Produção",
                            salario = 2000.00,
                            data_admissao = date.today())

    print(funcionario)

if __name__ == "__main__":
    main()



    