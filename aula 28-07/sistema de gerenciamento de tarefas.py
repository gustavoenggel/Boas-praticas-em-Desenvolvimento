#sistema de gerenciamento de tarefas

def exibir_menu():
    """Exibir o menu principal do sistema"""
    print("\n"+"="*30)
    print("Sistemas de tarefas")
    print("="*30)
    print("1. Listar tarefa")
    print("2. Adicionar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    print("="*30)

#FUNÇÃO DE LISTAR TAREFAS
def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas e seus status."""
    print("\n --- LISTA DE TAREFAS --- ")
    if not tarefas:
        print("Sem tarefas")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "concluido" if tarefa["concluido"] else ["pendente"]
        print(f"{indice}. {status} {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    """Adicionar uma nova tarefa a lista"""
    descricao = input("\nDigite a descricao da tarefa: ")
    if descricao:
        nova_tarefa ={"descricao": descricao, "concluido":False}
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso")
    else:
        print("A descrição nao pode estar vazia.")

def concluir_tarefa(tarefas):
    """Marcar tarefa como concluida"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        escolha = int(input("\nDigite o numero da tarefa que deseja concluir:"))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha -1]["concluido"] = True
            print("Tarefa marcada como concluida!")
        else:
            print("Numero de tarefas invalido.")
    except ValueError:
        print("Por favor,digite um numero valido!!")

def remover_tarefa(tarefas):
    """Remover tarefas da lista"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        escolha = int(input("\nDigite o numero da tarefa que deseja remover:"))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha -1)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
        else:
            print("Numero de tarefas invalido.")

    except ValueError:
        print("Por favor,digite um numero valido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        escolha = input("Escolha uma opcao: ")
        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida. Tente novamente.")

main()

