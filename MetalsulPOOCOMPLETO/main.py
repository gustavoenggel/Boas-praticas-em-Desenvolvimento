from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioDAO

from models.fornecedor import Fornecedor
from repositories.fornecedor_repository import FornecedorDAO

from models.cliente import Cliente
from repositories.cliente_repository import ClienteDAO

from models.usuario import Usuario
from repositories.usuario_repository import UsuarioDAO

from models.produto import Produto
from repositories.produto_repository import ProdutoDAO

from models.categoria_produto import CategoriaProduto
from repositories.categoria_repository import CategoriaProdutoDAO

from models.item_pedido_compra import ItemPedidoCompra
from repositories.item_pedido_compra_repository import ItemPedidoCompraDAO

from models.pedido_compra import PedidoCompra
from repositories.pedido_compra_repository import PedidoCompraDAO

from models.pedido_venda import PedidoVenda
from repositories.pedido_venda_repository import PedidoVendaDAO

from models.item_pedido_venda import ItemPedidoVenda
from repositories.item_pedido_venda_repository import ItemPedidoVendaDAO

# ==========================================================
# SUBMENU: FUNCIONÁRIOS
# ==========================================================
def exibir_menu_funcionario():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE FUNCIONÁRIOS ".center(40))
    print("=" * 40)
    print("1. Inserir novo funcionário")
    print("2. Listar todos os funcionários")
    print("3. Buscar funcionário por ID")
    print("4. Excluir funcionário")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_funcionario():
    dao = FuncionarioDAO()

    while True:
        exibir_menu_funcionario()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Funcionário ---")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            cargo = input("Cargo: ")

            novo_funcionario = Funcionario(
                nome=nome,
                cpf=cpf,
                rg="00.000.000-0",
                data_nascimento="1990-01-01",
                sexo="M",
                estado_civil="Solteiro",
                email=f"{nome.lower().replace(' ', '.')}@email.com",
                telefone="0000000000",
                celular="00000000000",
                cargo=cargo,
                departamento="Geral",
                salario=3000.00,
                data_admissao="2026-08-07",
                data_demissao=None,
                turno="Comercial",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_funcionario)

        elif opcao == "2":
            print("\n--- Lista de Funcionários ---")
            funcionarios = dao.buscar_todos()
            if funcionarios:
                for f in funcionarios:
                    f_id = getattr(f, 'id_funcionario', 'N/A')
                    print(f"ID: {f_id} | Nome: {f.nome} | CPF: {f.cpf} | Cargo: {f.cargo}")
            else:
                print("Nenhum funcionário cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Funcionário ---")
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
                resultado = dao.buscarFuncionario(id_busca)
                if resultado:
                    print(f"Funcionário encontrado: {resultado}")
                else:
                    print("Funcionário não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Funcionário ---")
            try:
                id_exclusao = int(input("Digite o ID do funcionário a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirFuncionario(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: FORNECEDORES
# ==========================================================
def exibir_menu_fornecedor():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE FORNECEDORES ".center(40))
    print("=" * 40)
    print("1. Inserir novo fornecedor")
    print("2. Listar todos os fornecedores")
    print("3. Buscar fornecedor por ID")
    print("4. Excluir fornecedor")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_fornecedor():
    dao = FornecedorDAO()

    while True:
        exibir_menu_fornecedor()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Fornecedor ---")
            razao_social = input("Razão Social: ")
            nome_fantasia = input("Nome Fantasia: ")
            cnpj = input("CNPJ (14 dígitos): ")

            novo_fornecedor = Fornecedor(
                razao_social=razao_social,
                nome_fantasia=nome_fantasia,
                cnpj=cnpj,
                inscricao_estadual="123456789",
                email=f"{razao_social.lower().replace(' ', '')}@fornecedor.com",
                telefone="0000000000",
                celular="00000000000",
                site="www.fornecedor.com",
                cep="00000000",
                endereco="Rua do Fornecedor",
                numero="100",
                complemento="",
                bairro="Industrial",
                cidade="Cidade",
                estado="UF",
                pais="Brasil",
                nome_contato="Contato Comercial",
                cargo_contato="Vendedor",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_fornecedor)

        elif opcao == "2":
            print("\n--- Lista de Fornecedores ---")
            fornecedores = dao.buscar_todos()
            if fornecedores:
                for f in fornecedores:
                    f_id = getattr(f, 'id_fornecedor', 'N/A')
                    print(
                        f"ID: {f_id} | Razão Social: {f.razao_social} | CNPJ: {f.cnpj} | Nome Fantasia: {f.nome_fantasia}")
            else:
                print("Nenhum fornecedor cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Fornecedor ---")
            try:
                id_busca = int(input("Digite o ID do fornecedor: "))
                resultado = dao.buscarFornecedor(id_busca)
                if resultado:
                    print(f"Fornecedor encontrado: {resultado}")
                else:
                    print("Fornecedor não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Fornecedor ---")
            try:
                id_exclusao = int(input("Digite o ID do fornecedor a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirFornecedor(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: CLIENTES
# ==========================================================
def exibir_menu_cliente():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE CLIENTES ".center(40))
    print("=" * 40)
    print("1. Inserir novo cliente")
    print("2. Listar todos os clientes")
    print("3. Buscar cliente por ID")
    print("4. Excluir cliente")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_cliente():
    dao = ClienteDAO()

    while True:
        exibir_menu_cliente()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Cliente ---")
            nome = input("Nome: ")
            cpf_cnpj = input("CPF/CNPJ (apenas números): ")
            tipo_cliente = input("Tipo (PF/PJ) [Padrão: PF]: ").upper() or "PF"

            novo_cliente = Cliente(
                tipo_cliente=tipo_cliente,
                nome=nome,
                cpf_cnpj=cpf_cnpj,
                inscricao_estadual="",
                email=f"{nome.lower().replace(' ', '.')}@cliente.com",
                telefone="0000000000",
                celular="00000000000",
                cep="00000000",
                endereco="Rua do Cliente",
                numero="50",
                complemento="",
                bairro="Centro",
                cidade="Cidade",
                estado="UF",
                pais="Brasil",
                limite_credito=1000.00,
                data_cadastro="2026-08-07",
                status="ATIVO",
                observacoes="Inserido via menu interativo."
            )

            dao.inserir(novo_cliente)

        elif opcao == "2":
            print("\n--- Lista de Clientes ---")
            clientes = dao.buscar_todos()
            if clientes:
                for c in clientes:
                    c_id = getattr(c, 'id_cliente', 'N/A')
                    print(f"ID: {c_id} | Nome: {c.nome} | Tipo: {c.tipo_cliente} | CPF/CNPJ: {c.cpf_cnpj}")
            else:
                print("Nenhum cliente cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Cliente ---")
            try:
                id_busca = int(input("Digite o ID do cliente: "))
                resultado = dao.buscarCliente(id_busca)
                if resultado:
                    print(f"Cliente encontrado: {resultado}")
                else:
                    print("Cliente não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Cliente ---")
            try:
                id_exclusao = int(input("Digite o ID do cliente a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirCliente(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: USUÁRIOS
# ==========================================================
def exibir_menu_usuario():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE USUÁRIOS ".center(40))
    print("=" * 40)
    print("1. Inserir novo usuário")
    print("2. Listar todos os usuários")
    print("3. Buscar usuário por ID")
    print("4. Excluir usuário")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_usuario():
    dao = UsuarioDAO()

    while True:
        exibir_menu_usuario()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Usuário ---")
            usuario_login = input("Nome de usuário (login): ")
            senha_hash = input("Senha (ou hash): ")
            nivel = input(
                "Nível de acesso (ADMIN, GERENTE, ESTOQUE, VENDAS, COMPRAS, OPERADOR) [Padrão: OPERADOR]: ").upper() or "OPERADOR"

            try:
                id_funcionario = int(input("ID do Funcionário vinculado: "))
            except ValueError:
                print("Por favor, insira um ID de funcionário válido.")
                continue

            novo_usuario = Usuario(
                usuario=usuario_login,
                senha_hash=senha_hash,
                nivel_acesso=nivel,
                ultimo_login=None,
                ativo=True,
                id_funcionario=id_funcionario
            )

            dao.inserir(novo_usuario)

        elif opcao == "2":
            print("\n--- Lista de Usuários ---")
            usuarios = dao.buscar_todos()
            if usuarios:
                for u in usuarios:
                    u_id = getattr(u, 'id_usuario', 'N/A')
                    print(
                        f"ID: {u_id} | Usuário: {u.usuario} | Nível: {u.nivel_acesso} | ID Func.: {u.id_funcionario} | Ativo: {u.ativo}")
            else:
                print("Nenhum usuário cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Usuário ---")
            try:
                id_busca = int(input("Digite o ID do usuário: "))
                resultado = dao.buscarUsuario(id_busca)
                if resultado:
                    print(f"Usuário encontrado: {resultado}")
                else:
                    print("Usuário não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Usuário ---")
            try:
                id_exclusao = int(input("Digite o ID do usuário a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirUsuario(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: PRODUTOS
# ==========================================================
def exibir_menu_produto():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE PRODUTOS ".center(40))
    print("=" * 40)
    print("1. Inserir novo produto")
    print("2. Listar todos os produtos")
    print("3. Buscar produto por ID")
    print("4. Excluir produto")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_produto():
    dao = ProdutoDAO()

    while True:
        exibir_menu_produto()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Produto ---")
            codigo = input("Código do produto: ")
            descricao = input("Descrição: ")

            try:
                preco_custo = float(input("Preço de custo (R$): "))
                preco_venda = float(input("Preço de venda (R$): "))
                id_categoria = int(input("ID da Categoria: "))
                id_fornecedor = int(input("ID do Fornecedor: "))
            except ValueError:
                print("Valores numéricos inválidos fornecidos. Tente novamente.")
                continue

            novo_produto = Produto(
                codigo=codigo,
                codigo_barras=f"789{codigo}",
                descricao=descricao,
                unidade_medida="UN",
                marca="Generica",
                modelo="Padrao",
                fabricante="Fabricante X",
                peso=1.0,
                altura=10.0,
                largura=10.0,
                comprimento=10.0,
                cor="Preto",
                preco_custo=preco_custo,
                preco_venda=preco_venda,
                margem_lucro=((preco_venda - preco_custo) / preco_custo * 100) if preco_custo > 0 else 0,
                estoque_atual=10,
                estoque_minimo=2,
                estoque_maximo=50,
                localizacao="Aisle 1",
                lote="L01",
                data_fabricacao=None,
                data_validade=None,
                data_cadastro="2026-08-07",
                ativo=True,
                id_categoria=id_categoria,
                id_fornecedor=id_fornecedor
            )

            dao.inserir(novo_produto)

        elif opcao == "2":
            print("\n--- Lista de Produtos ---")
            produtos = dao.buscar_todos()
            if produtos:
                for p in produtos:
                    p_id = getattr(p, 'id_produto', 'N/A')
                    print(
                        f"ID: {p_id} | Código: {p.codigo} | Descrição: {p.descricao} | Preço Venda: R${p.preco_venda:.2f} | Estoque: {p.estoque_atual}")
            else:
                print("Nenhum produto cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Produto ---")
            try:
                id_busca = int(input("Digite o ID do produto: "))
                resultado = dao.buscarProduto(id_busca)
                if resultado:
                    print(f"Produto encontrado: {resultado}")
                else:
                    print("Produto não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Produto ---")
            try:
                id_exclusao = int(input("Digite o ID do produto a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirProduto(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# ==========================================================
# SUBMENU: CATEGORIAS DE PRODUTO
# ==========================================================
def exibir_menu_categoria():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE CATEGORIAS ".center(40))
    print("=" * 40)
    print("1. Inserir nova categoria")
    print("2. Listar todas as categorias")
    print("3. Buscar categoria por ID")
    print("4. Excluir categoria")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_categoria():
    dao = CategoriaProdutoDAO()

    while True:
        exibir_menu_categoria()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Categoria ---")
            nome = input("Nome da categoria: ")
            descricao = input("Descrição: ")

            nova_categoria = CategoriaProduto(
                nome=nome,
                descricao=descricao,
                ativo=True
            )

            dao.inserir(nova_categoria)

        elif opcao == "2":
            print("\n--- Lista de Categorias ---")
            categorias = dao.buscar_todos()
            if categorias:
                for c in categorias:
                    c_id = getattr(c, 'id_categoria', 'N/A')
                    print(f"ID: {c_id} | Nome: {c.nome} | Descrição: {c.descricao} | Ativa: {c.ativo}")
            else:
                print("Nenhuma categoria cadastrada ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Categoria ---")
            try:
                id_busca = int(input("Digite o ID da categoria: "))
                resultado = dao.buscarCategoria(id_busca)
                if resultado:
                    print(f"Categoria encontrada: {resultado}")
                else:
                    print("Categoria não encontrada com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Categoria ---")
            try:
                id_exclusao = int(input("Digite o ID da categoria a ser excluída: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirCategoria(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# ==========================================================
# SUBMENU: ITENS DE PEDIDO DE COMPRA
# ==========================================================
def exibir_menu_item_pedido_compra():
    print("\n" + "=" * 40)
    print(" ITENS DO PEDIDO DE COMPRA ".center(40))
    print("=" * 40)
    print("1. Inserir novo item no pedido")
    print("2. Listar todos os itens")
    print("3. Buscar item por ID")
    print("4. Excluir item do pedido")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_item_pedido_compra():
    dao = ItemPedidoCompraDAO()

    while True:
        exibir_menu_item_pedido_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Item no Pedido ---")
            try:
                id_pedido_compra = int(input("ID do Pedido de Compra: "))
                id_produto = int(input("ID do Produto: "))
                quantidade = int(input("Quantidade: "))
                preco_unitario = float(input("Preço Unitário (R$): "))
                desconto = float(input("Desconto (R$) [Padrão: 0.0]: ") or 0.0)
            except ValueError:
                print("Valores numéricos inválidos fornecidos. Tente novamente.")
                continue

            subtotal = (quantidade * preco_unitario) - desconto

            novo_item = ItemPedidoCompra(
                id_pedido_compra=id_pedido_compra,
                id_produto=id_produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                desconto=desconto,
                subtotal=subtotal
            )

            dao.inserir(novo_item)

        elif opcao == "2":
            print("\n--- Lista de Itens de Pedidos de Compra ---")
            itens = dao.buscar_todos()
            if itens:
                for i in itens:
                    i_id = getattr(i, 'id_item_pedido', 'N/A')
                    print(f"ID: {i_id} | Pedido: {i.id_pedido_compra} | Produto: {i.id_produto} | Qtd: {i.quantidade} | Subtotal: R${i.subtotal:.2f}")
            else:
                print("Nenhum item cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Item por ID ---")
            try:
                id_busca = int(input("Digite o ID do item de pedido: "))
                resultado = dao.buscarItemPedido(id_busca)
                if resultado:
                    print(f"Item encontrado: {resultado}")
                else:
                    print("Item não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Item do Pedido ---")
            try:
                id_exclusao = int(input("Digite o ID do item a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirItemPedido(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: PEDIDOS DE COMPRA
# ==========================================================
def exibir_menu_pedido_compra():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE PEDIDOS DE COMPRA ".center(40))
    print("=" * 40)
    print("1. Inserir novo pedido de compra")
    print("2. Listar todos os pedidos de compra")
    print("3. Buscar pedido por ID")
    print("4. Excluir pedido de compra")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_pedido_compra():
    dao = PedidoCompraDAO()

    while True:
        exibir_menu_pedido_compra()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Pedido de Compra ---")
            numero_pedido = input("Número do Pedido (ex: PC-001): ")
            forma_pagamento = input("Forma de Pagamento (ex: Boleto, PIX, Cartão): ")

            try:
                id_fornecedor = int(input("ID do Fornecedor: "))
                id_funcionario = int(input("ID do Funcionário: "))
                valor_total = float(input("Valor Total (R$) [Padrão: 0.0]: ") or 0.0)
                valor_desconto = float(input("Valor do Desconto (R$) [Padrão: 0.0]: ") or 0.0)
            except ValueError:
                print("Valores numéricos inválidos fornecidos. Tente novamente.")
                continue

            novo_pedido = PedidoCompra(
                numero_pedido=numero_pedido,
                data_pedido="2026-08-07",
                data_entrega_prevista="2026-08-15",
                status="PENDENTE",
                valor_total=valor_total,
                valor_desconto=valor_desconto,
                forma_pagamento=forma_pagamento,
                observacoes="Criado via menu interativo.",
                id_fornecedor=id_fornecedor,
                id_funcionario=id_funcionario
            )

            dao.inserir(novo_pedido)

        elif opcao == "2":
            print("\n--- Lista de Pedidos de Compra ---")
            pedidos = dao.buscar_todos()
            if pedidos:
                for p in pedidos:
                    p_id = getattr(p, 'id_pedido_compra', 'N/A')
                    print(
                        f"ID: {p_id} | Nº: {p.numero_pedido} | Status: {p.status} | Total: R${p.valor_total:.2f} | Fornecedor ID: {p.id_fornecedor}")
            else:
                print("Nenhum pedido de compra cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Pedido por ID ---")
            try:
                id_busca = int(input("Digite o ID do pedido de compra: "))
                resultado = dao.buscarPedidoCompra(id_busca)
                if resultado:
                    print(f"Pedido encontrado: {resultado}")
                else:
                    print("Pedido não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Pedido de Compra ---")
            try:
                id_exclusao = int(input("Digite o ID do pedido a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirPedidoCompra(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# SUBMENU: PEDIDOS DE VENDA
# ==========================================================
def exibir_menu_pedido_venda():
    print("\n" + "=" * 40)
    print(" GERENCIAMENTO DE PEDIDOS DE VENDA ".center(40))
    print("=" * 40)
    print("1. Inserir novo pedido de venda")
    print("2. Listar todos os pedidos de venda")
    print("3. Buscar pedido por ID")
    print("4. Excluir pedido de venda")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_pedido_venda():
    dao = PedidoVendaDAO()

    while True:
        exibir_menu_pedido_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Pedido de Venda ---")
            numero_pedido = input("Número do Pedido (ex: PV-001): ")
            forma_pagamento = input("Forma de Pagamento (ex: Cartão, Pix, Dinheiro): ")

            try:
                id_cliente = int(input("ID do Cliente: "))
                id_funcionario = int(input("ID do Funcionário (Vendedor): "))
                valor_total = float(input("Valor Total (R$) [Padrão: 0.0]: ") or 0.0)
                valor_desconto = float(input("Valor do Desconto (R$) [Padrão: 0.0]: ") or 0.0)
            except ValueError:
                print("Valores numéricos inválidos fornecidos. Tente novamente.")
                continue

            novo_pedido = PedidoVenda(
                numero_pedido=numero_pedido,
                data_pedido="2026-08-07",
                data_entrega="2026-08-10",
                status="PENDENTE",
                valor_total=valor_total,
                valor_desconto=valor_desconto,
                forma_pagamento=forma_pagamento,
                observacoes="Criado via menu interativo.",
                id_cliente=id_cliente,
                id_funcionario=id_funcionario
            )

            dao.inserir(novo_pedido)

        elif opcao == "2":
            print("\n--- Lista de Pedidos de Venda ---")
            pedidos = dao.buscar_todos()
            if pedidos:
                for p in pedidos:
                    p_id = getattr(p, 'id_pedido_venda', 'N/A')
                    print(
                        f"ID: {p_id} | Nº: {p.numero_pedido} | Status: {p.status} | Total: R${p.valor_total:.2f} | Cliente ID: {p.id_cliente}")
            else:
                print("Nenhum pedido de venda cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Pedido por ID ---")
            try:
                id_busca = int(input("Digite o ID do pedido de venda: "))
                resultado = dao.buscarPedidoVenda(id_busca)
                if resultado:
                    print(f"Pedido encontrado: {resultado}")
                else:
                    print("Pedido não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Pedido de Venda ---")
            try:
                id_exclusao = int(input("Digite o ID do pedido a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirPedidoVenda(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# ==========================================================
# SUBMENU: ITENS DE PEDIDO DE VENDA
# ==========================================================
def exibir_menu_item_pedido_venda():
    print("\n" + "=" * 40)
    print(" ITENS DO PEDIDO DE VENDA ".center(40))
    print("=" * 40)
    print("1. Inserir novo item no pedido de venda")
    print("2. Listar todos os itens")
    print("3. Buscar item por ID")
    print("4. Excluir item do pedido")
    print("0. Voltar ao menu principal")
    print("=" * 40)


def menu_item_pedido_venda():
    dao = ItemPedidoVendaDAO()

    while True:
        exibir_menu_item_pedido_venda()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("\n--- Inserir Item no Pedido de Venda ---")
            try:
                id_pedido_venda = int(input("ID do Pedido de Venda: "))
                id_produto = int(input("ID do Produto: "))
                quantidade = int(input("Quantidade: "))
                preco_unitario = float(input("Preço Unitário (R$): "))
                desconto = float(input("Desconto (R$) [Padrão: 0.0]: ") or 0.0)
            except ValueError:
                print("Valores numéricos inválidos fornecidos. Tente novamente.")
                continue

            subtotal = (quantidade * preco_unitario) - desconto

            novo_item = ItemPedidoVenda(
                id_pedido_venda=id_pedido_venda,
                id_produto=id_produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                desconto=desconto,
                subtotal=subtotal
            )

            dao.inserir(novo_item)

        elif opcao == "2":
            print("\n--- Lista de Itens de Pedidos de Venda ---")
            itens = dao.buscar_todos()
            if itens:
                for i in itens:
                    i_id = getattr(i, 'id_item_venda', 'N/A')
                    print(f"ID: {i_id} | Pedido Venda: {i.id_pedido_venda} | Produto: {i.id_produto} | Qtd: {i.quantidade} | Subtotal: R${i.subtotal:.2f}")
            else:
                print("Nenhum item cadastrado ou erro ao buscar.")

        elif opcao == "3":
            print("\n--- Buscar Item por ID ---")
            try:
                id_busca = int(input("Digite o ID do item de venda: "))
                resultado = dao.buscarItemVenda(id_busca)
                if resultado:
                    print(f"Item encontrado: {resultado}")
                else:
                    print("Item não encontrado com este ID.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "4":
            print("\n--- Excluir Item do Pedido de Venda ---")
            try:
                id_exclusao = int(input("Digite o ID do item a ser excluído: "))
                confirmacao = input(f"Tem certeza que deseja excluir o ID {id_exclusao}? (S/N): ").upper()
                if confirmacao == 'S':
                    dao.ExcluirItemVenda(id_exclusao)
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("Por favor, digite um número válido para o ID.")

        elif opcao == "0":
            dao.fechar()
            break

        else:
            print("\nOpção inválida. Tente novamente.")