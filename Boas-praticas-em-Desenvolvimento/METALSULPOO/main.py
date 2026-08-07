from models.funcionario import Funcionario
from models.setor import Setor

setor1 = Setor(1,"TA")
funcionario1 = Funcionario(1,"Joaquim","Dev",5500.00,setor1)
funcionario1.aumentar_salario(200)
funcionario1.apresentar()













"""
print("-"*30)
setor1.nome = "Tech"
setor1.apresentar
setor1.nome = ""
"""


"""
print()
print(funcionario1.get_nome())
print(funcionario1.get_id())
print(funcionario1.get_cargo())
print(funcionario1.get_salario())
funcionario1.set_nome("Joao pedro silva valentim")
funcionario1.set_cargo("Professor")
funcionario1.set_salario(6900)
funcionario1.apresentar()
"""