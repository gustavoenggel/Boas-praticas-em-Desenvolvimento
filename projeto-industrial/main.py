from funcionario import listar_funcionarios

from funcionario import cadastrar_funcionario

from funcionario import atualizar_cargo

from funcionario import deletar_funcionario

from setor import criar_setor
from setor  import atualizar_setor
from setor import deletar_setor,listar_setores

#atualizar_cargo(4, "Técnico em Automação")
#listar_funcionarios()
#cadastrar_funcionarios(cargo,id_setor)
#atualizar_funcionario
#deletar_funcionario(2)
#criar_setor("Ferramentaria")
#atualizar_setor(1,"Usinagem")
#deletar_setor(2)
#listar_setores()


#cadastrar_funcionario('pedro', 'tecnico', 3, '10101010102', '2000', '2024-09-09')
#atualizar_cargo(4, "Técnico em Automação")
#listar_funcionarios()

#criar_setor('TI','SUL')
#listar_setores()
#atualizar_setor(5,'Almoxarifado','Sudeste')
#listar_setores()

while True:
    print('\n----SISTEMA INDUSTRIAL----')
    print('1 - Listar Funcionario')
    print('2 - Cadastrar Funcionario')
    print('3 - Atualizar Salario')
    print('4 - Remover Funcionario')
    print('5 - Sair')

    opcao = input('Escolha uma opção:')
    
    if opcao == '1':


    elif opcao =='2':
        nome = input('NOME:')
        cpf = input('CPF:')

    elif opcao == '3':
        id_funcionario = input('ID funcionario:')
        novo_cargo = input('Cargo:')

        atualizar_cargo(id_funcionario,novo_cargo)

    elif opcao == '4':
        id_funcionario = input('ID Funcionario:')

        deletar_funcionario(id_funcionario)
    
    #sair
    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Tente novamente')
