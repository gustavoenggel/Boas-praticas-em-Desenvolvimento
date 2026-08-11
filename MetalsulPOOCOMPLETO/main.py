from models.funcionario import Funcionario
from models.fornecedor import Fornecedor
from models.cliente import Cliente
from models.usuario import Usuario
from models.produto import Produto
from models.categoria_produto import CategoriaProduto
from models.pedido_compra import PedidoCompra
from models.item_pedido_compra import ItemPedidoCompra
from models.pedido_venda import PedidoVenda
from models.item_pedido_venda import ItemPedidoVenda

from repositories.funcionario_repository import FuncionarioRepository
from repositories.fornecedor_repository import FornecedorDAO
from repositories.cliente_repository import ClienteDAO
from repositories.usuario_repository import UsuarioDAO
from repositories.produto_repository import ProdutoDAO
from repositories.categoria_repository import CategoriaProdutoDAO
from repositories.pedido_compra_repository import PedidoCompraDAO
from repositories.item_pedido_compra_repository import ItemPedidoCompraDAO
from repositories.pedido_venda_repository import PedidoVendaDAO
from repositories.item_pedido_venda_repository import ItemPedidoVendaDAO

from menu import (
    exibir_menu_principal,
    exibir_menu_funcionario,
    exibir_menu_fornecedor,
    exibir_menu_cliente,
    exibir_menu_usuario,
    exibir_menu_produto,
    exibir_menu_categoria,
    exibir_menu_pedido_compra,
    exibir_menu_item_pedido_compra,
    exibir_menu_pedido_venda,
    exibir_menu_item_pedido_venda
)


# ==========================================================
# LÓGICA DOS SUBMENUS
# ==========================================================
def menu_funcionario():
    dao = FuncionarioRepository()
    while True:
        exibir_menu_funcionario()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Funcionário ---")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cargo = input("Cargo: ")
            departamento = input("Departamento: ")
            try:
                salario = float(input("Salário (R$): ") or 0.0)
            except ValueError:
                print("Valor numérico inválido.")
                continue

            novo = Funcionario(
                nome=nome, cpf=cpf, cargo=cargo,
                departamento=departamento, salario=salario,
                data_admissao="2026-08-11"
            )
            dao.inserir(novo)

        elif opcao == "2":
            print("\n--- Lista de Funcionários ---")
            for f in dao.buscar_todos():
                print(f"ID: {f.id_funcionario} | Nome: {f.nome} | Cargo: {f.cargo}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do funcionário: "))
                print(dao.buscarFuncionario(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirFuncionario(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_fornecedor():
    dao = FornecedorDAO()
    while True:
        exibir_menu_fornecedor()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            razao = input("Razão Social: ")
            cnpj = input("CNPJ: ")
            novo = Fornecedor(razao_social=razao, cnpj=cnpj)
            dao.inserir(novo)

        elif opcao == "2":
            for f in dao.buscar_todos():
                f_id = getattr(f, 'id_fornecedor', 'N/A')
                f_razao = getattr(f, 'razao_social', 'N/A')
                print(f"ID: {f_id} | Razão Social: {f_razao}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do fornecedor: "))
                print(dao.buscarFornecedor(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirFornecedor(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_cliente():
    dao = ClienteDAO()
    while True:
        exibir_menu_cliente()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf_cnpj = input("CPF/CNPJ: ")
            novo = Cliente(nome=nome, cpf_cnpj=cpf_cnpj)
            dao.inserir(novo)

        elif opcao == "2":
            for c in dao.buscar_todos():
                c_id = getattr(c, 'id_cliente', 'N/A')
                c_nome = getattr(c, 'nome', 'N/A')
                print(f"ID: {c_id} | Nome: {c_nome}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do cliente: "))
                print(dao.buscarCliente(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirCliente(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_usuario():
    dao = UsuarioDAO()
    while True:
        exibir_menu_usuario()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            usr = input("Usuário: ")
            senha = input("Senha: ")
            try:
                id_func = int(input("ID Funcionário: "))
            except ValueError:
                print("ID inválido.")
                continue
            novo = Usuario(usuario=usr, senha_hash=senha, nivel_acesso="OPERADOR", id_funcionario=id_func)
            dao.inserir(novo)

        elif opcao == "2":
            for u in dao.buscar_todos():
                u_id = getattr(u, 'id_usuario', 'N/A')
                u_nome = getattr(u, 'usuario', 'N/A')
                print(f"ID: {u_id} | Usuário: {u_nome}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do usuário: "))
                print(dao.buscarUsuario(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirUsuario(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_produto():
    dao = ProdutoDAO()
    while True:
        exibir_menu_produto()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            codigo = input("Código: ")
            descricao = input("Descrição: ")
            unidade = input("Unidade de Medida: ")
            try:
                custo = float(input("Preço de Custo (R$): ") or 0.0)
                venda = float(input("Preço de Venda (R$): ") or 0.0)
                id_cat = int(input("ID Categoria: "))
                id_forn = int(input("ID Fornecedor: "))
            except ValueError:
                print("Valores inválidos.")
                continue

            novo = Produto(
                codigo=codigo, descricao=descricao, unidade_medida=unidade,
                preco_custo=custo, preco_venda=venda, id_categoria=id_cat, id_fornecedor=id_forn
            )
            dao.inserir(novo)

        elif opcao == "2":
            for p in dao.buscar_todos():
                p_id = getattr(p, 'id_produto', 'N/A')
                p_desc = getattr(p, 'descricao', 'N/A')
                print(f"ID: {p_id} | Descrição: {p_desc}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do produto: "))
                print(dao.buscarProduto(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirProduto(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_categoria():
    dao = CategoriaProdutoDAO()
    while True:
        exibir_menu_categoria()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            nome = input("Nome da Categoria: ")
            descricao = input("Descrição: ")
            novo = CategoriaProduto(nome=nome, descricao=descricao)
            dao.inserir(novo)

        elif opcao == "2":
            for c in dao.buscar_todos():
                c_id = getattr(c, 'id_categoria', 'N/A')
                c_nome = getattr(c, 'nome', 'N/A')
                print(f"ID: {c_id} | Nome: {c_nome}")

        elif opcao == "3":
            try:
                id_b = int(input("ID da categoria: "))
                print(dao.buscarCategoriaProduto(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirCategoriaProduto(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_pedido_compra():
    dao = PedidoCompraDAO()
    while True:
        exibir_menu_pedido_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            num = input("Número do Pedido: ")
            try:
                id_forn = int(input("ID Fornecedor: "))
                id_func = int(input("ID Funcionário: "))
            except ValueError:
                print("Valores inválidos.")
                continue

            novo = PedidoCompra(numero_pedido=num, id_fornecedor=id_forn, id_funcionario=id_func)
            dao.inserir(novo)

        elif opcao == "2":
            for p in dao.buscar_todos():
                p_id = getattr(p, 'id_pedido_compra', 'N/A')
                p_num = getattr(p, 'numero_pedido', 'N/A')
                print(f"ID: {p_id} | Nº: {p_num}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do pedido: "))
                print(dao.buscarPedidoCompra(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirPedidoCompra(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_item_pedido_compra():
    dao = ItemPedidoCompraDAO()
    while True:
        exibir_menu_item_pedido_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            try:
                id_pc = int(input("ID Pedido Compra: "))
                id_prod = int(input("ID Produto: "))
                qtd = int(input("Quantidade: "))
                valor = float(input("Valor Unitário (R$): "))
            except ValueError:
                print("Valores inválidos.")
                continue

            subtotal = qtd * valor
            novo = ItemPedidoCompra(
                id_pedido_compra=id_pc, id_produto=id_prod,
                quantidade=qtd, valor_unitario=valor, subtotal=subtotal
            )
            dao.inserir(novo)

        elif opcao == "2":
            for i in dao.buscar_todos():
                i_id = getattr(i, 'id_item_compra', 'N/A')
                print(f"ID Item Compra: {i_id}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do item: "))
                print(dao.buscarItemCompra(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirItemCompra(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_pedido_venda():
    dao = PedidoVendaDAO()
    while True:
        exibir_menu_pedido_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            num = input("Número do Pedido (ex: PV-001): ")
            forma = input("Forma de Pagamento: ")
            try:
                id_cli = int(input("ID Cliente: "))
                id_func = int(input("ID Funcionário: "))
                total = float(input("Valor Total (R$) [Padrão 0.0]: ") or 0.0)
                desc = float(input("Desconto (R$) [Padrão 0.0]: ") or 0.0)
            except ValueError:
                print("Valores inválidos.")
                continue

            novo = PedidoVenda(
                numero_pedido=num, valor_total=total, desconto=desc,
                forma_pagamento=forma, status="ABERTO", id_cliente=id_cli, id_funcionario=id_func
            )
            dao.inserir(novo)

        elif opcao == "2":
            for p in dao.buscar_todos():
                print(f"ID: {p.id_pedido_venda} | Nº: {p.numero_pedido} | Status: {p.status} | Total: R${p.valor_total:.2f}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do pedido: "))
                print(dao.buscarPedidoVenda(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirPedidoVenda(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


def menu_item_pedido_venda():
    dao = ItemPedidoVendaDAO()
    while True:
        exibir_menu_item_pedido_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            try:
                id_pv = int(input("ID Pedido Venda: "))
                id_prod = int(input("ID Produto: "))
                qtd = int(input("Quantidade: "))
                preco = float(input("Preço Unitário (R$): "))
                desc = float(input("Desconto (R$) [Padrão 0.0]: ") or 0.0)
            except ValueError:
                print("Valores inválidos.")
                continue

            subtotal = (qtd * preco) - desc
            novo = ItemPedidoVenda(
                id_pedido_venda=id_pv, id_produto=id_prod,
                quantidade=qtd, preco_unitario=preco, desconto=desc, subtotal=subtotal
            )
            dao.inserir(novo)

        elif opcao == "2":
            for i in dao.buscar_todos():
                i_id = getattr(i, 'id_item_venda', 'N/A')
                print(f"ID: {i_id} | Pedido Venda: {i.id_pedido_venda} | Produto: {i.id_produto} | Subtotal: R${i.subtotal:.2f}")

        elif opcao == "3":
            try:
                id_b = int(input("ID do item: "))
                print(dao.buscarItemVenda(id_b) or "Não encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_e = int(input("ID a excluir: "))
                dao.ExcluirItemVenda(id_e)
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            dao.fechar()
            break


# ==========================================================
# LOOP PRINCIPAL DO SISTEMA
# ==========================================================
def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha o módulo desejado: ")

        if opcao == "1":
            menu_funcionario()
        elif opcao == "2":
            menu_fornecedor()
        elif opcao == "3":
            menu_cliente()
        elif opcao == "4":
            menu_usuario()
        elif opcao == "5":
            menu_produto()
        elif opcao == "6":
            menu_categoria()
        elif opcao == "7":
            menu_pedido_compra()
        elif opcao == "8":
            menu_item_pedido_compra()
        elif opcao == "9":
            menu_pedido_venda()
        elif opcao == "10":
            menu_item_pedido_venda()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()