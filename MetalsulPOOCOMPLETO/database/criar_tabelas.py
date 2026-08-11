from database.conexao import Conexao


def criar_tabelas():
    # Aqui colocamos todo o seu script SQL dentro de uma string tripla (docstring)
    script_sql = """
    -- ==========================================================
    -- GARANTIR O SCHEMA EMPRESA (Opcional, mas recomendado pelo seu .env)
    -- ==========================================================
    CREATE SCHEMA IF NOT EXISTS empresa;
    SET search_path TO empresa;

    -- ==========================================================
    -- TABELA FUNCIONARIO
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS funcionario (
        id_funcionario SERIAL PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        cpf CHAR(11) NOT NULL UNIQUE,
        rg VARCHAR(20),
        data_nascimento DATE,
        sexo CHAR(1) CHECK (sexo IN ('M','F')),
        estado_civil VARCHAR(30),
        email VARCHAR(150) UNIQUE,
        telefone VARCHAR(20),
        celular VARCHAR(20),
        cargo VARCHAR(80) NOT NULL,
        departamento VARCHAR(80) NOT NULL,
        salario NUMERIC(12,2) CHECK (salario >= 0),
        data_admissao DATE NOT NULL,
        data_demissao DATE,
        turno VARCHAR(30),
        status VARCHAR(20) DEFAULT 'ATIVO' CHECK(status IN ('ATIVO','INATIVO','AFASTADO','FERIAS')),
        observacoes TEXT
    );

    -- ==========================================================
    -- TABELA USUARIO
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS usuario (
        id_usuario SERIAL PRIMARY KEY,
        usuario VARCHAR(50) NOT NULL UNIQUE,
        senha_hash VARCHAR(255) NOT NULL,
        nivel_acesso VARCHAR(30) NOT NULL CHECK(nivel_acesso IN ('ADMIN', 'GERENTE', 'ESTOQUE', 'VENDAS', 'COMPRAS', 'OPERADOR')),
        ultimo_login TIMESTAMP,
        ativo BOOLEAN DEFAULT TRUE,
        id_funcionario INTEGER NOT NULL UNIQUE,
        CONSTRAINT fk_usuario_funcionario FOREIGN KEY(id_funcionario) REFERENCES funcionario(id_funcionario) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    -- ==========================================================
    -- TABELA CLIENTE
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente SERIAL PRIMARY KEY,
        tipo_cliente VARCHAR(20) CHECK(tipo_cliente IN ('PF', 'PJ')),
        nome VARCHAR(150) NOT NULL,
        cpf_cnpj VARCHAR(14) UNIQUE,
        inscricao_estadual VARCHAR(30),
        email VARCHAR(150),
        telefone VARCHAR(20),
        celular VARCHAR(20),
        cep CHAR(8),
        endereco VARCHAR(150),
        numero VARCHAR(10),
        complemento VARCHAR(80),
        bairro VARCHAR(80),
        cidade VARCHAR(80),
        estado CHAR(2),
        pais VARCHAR(50) DEFAULT 'Brasil',
        limite_credito NUMERIC(12,2) DEFAULT 0 CHECK(limite_credito >= 0),
        data_cadastro DATE DEFAULT CURRENT_DATE,
        status VARCHAR(20) DEFAULT 'ATIVO' CHECK(status IN ('ATIVO', 'INATIVO')),
        observacoes TEXT
    );

    -- ==========================================================
    -- TABELA FORNECEDOR
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS fornecedor (
        id_fornecedor SERIAL PRIMARY KEY,
        razao_social VARCHAR(150) NOT NULL,
        nome_fantasia VARCHAR(150),
        cnpj CHAR(14) NOT NULL UNIQUE,
        inscricao_estadual VARCHAR(30),
        email VARCHAR(150),
        telefone VARCHAR(20),
        celular VARCHAR(20),
        site VARCHAR(150),
        cep CHAR(8),
        endereco VARCHAR(150),
        numero VARCHAR(10),
        complemento VARCHAR(80),
        bairro VARCHAR(80),
        cidade VARCHAR(80),
        estado CHAR(2),
        pais VARCHAR(50) DEFAULT 'Brasil',
        nome_contato VARCHAR(100),
        cargo_contato VARCHAR(80),
        status VARCHAR(20) DEFAULT 'ATIVO' CHECK (status IN ('ATIVO','INATIVO')),
        observacoes TEXT
    );

    -- ==========================================================
    -- TABELA CATEGORIA_PRODUTO
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS categoria_produto (
        id_categoria SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL UNIQUE,
        descricao TEXT,
        ativo BOOLEAN DEFAULT TRUE
    );

    -- ==========================================================
    -- TABELA PRODUTO
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS produto (
        id_produto SERIAL PRIMARY KEY,
        codigo VARCHAR(30) NOT NULL UNIQUE,
        codigo_barras VARCHAR(30) UNIQUE,
        descricao VARCHAR(200) NOT NULL,
        unidade_medida VARCHAR(20) NOT NULL,
        marca VARCHAR(60),
        modelo VARCHAR(60),
        fabricante VARCHAR(100),
        peso NUMERIC(10,3) CHECK (peso >= 0),
        altura NUMERIC(10,2) CHECK (altura >= 0),
        largura NUMERIC(10,2) CHECK (largura >= 0),
        comprimento NUMERIC(10,2) CHECK (comprimento >= 0),
        cor VARCHAR(30),
        preco_custo NUMERIC(12,2) NOT NULL CHECK (preco_custo >= 0),
        preco_venda NUMERIC(12,2) NOT NULL CHECK (preco_venda >= 0),
        margem_lucro NUMERIC(6,2) DEFAULT 0 CHECK (margem_lucro >= 0),
        estoque_atual INTEGER DEFAULT 0 CHECK (estoque_atual >= 0),
        estoque_minimo INTEGER DEFAULT 0 CHECK (estoque_minimo >= 0),
        estoque_maximo INTEGER DEFAULT 0 CHECK (estoque_maximo >= 0),
        localizacao VARCHAR(50),
        lote VARCHAR(40),
        data_fabricacao DATE,
        data_validade DATE,
        data_cadastro DATE DEFAULT CURRENT_DATE,
        ativo BOOLEAN DEFAULT TRUE,
        id_categoria INTEGER NOT NULL,
        id_fornecedor INTEGER NOT NULL,
        CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria) REFERENCES categoria_produto(id_categoria) ON UPDATE CASCADE ON DELETE RESTRICT,
        CONSTRAINT fk_produto_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    -- ==========================================================
    -- TABELA PEDIDO_COMPRA
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS pedido_compra (
        id_pedido_compra SERIAL PRIMARY KEY,
        numero_pedido VARCHAR(20) NOT NULL UNIQUE,
        data_emissao DATE DEFAULT CURRENT_DATE,
        data_prevista_entrega DATE,
        data_recebimento DATE,
        valor_total NUMERIC(14,2) DEFAULT 0 CHECK (valor_total >= 0),
        forma_pagamento VARCHAR(50),
        status VARCHAR(30) DEFAULT 'ABERTO' CHECK (status IN ('ABERTO', 'APROVADO', 'EM_TRANSITO', 'RECEBIDO', 'CANCELADO')),
        observacoes TEXT,
        id_fornecedor INTEGER NOT NULL,
        id_funcionario INTEGER NOT NULL,
        CONSTRAINT fk_pc_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor) ON UPDATE CASCADE ON DELETE RESTRICT,
        CONSTRAINT fk_pc_funcionario FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    -- ==========================================================
    -- TABELA ITEM_PEDIDO_COMPRA
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS item_pedido_compra (
        id_item_compra SERIAL PRIMARY KEY,
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        valor_unitario NUMERIC(12,2) NOT NULL CHECK (valor_unitario >= 0),
        desconto NUMERIC(12,2) DEFAULT 0 CHECK (desconto >= 0),
        subtotal NUMERIC(14,2) NOT NULL CHECK (subtotal >= 0),
        id_pedido_compra INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        CONSTRAINT fk_item_pc FOREIGN KEY (id_pedido_compra) REFERENCES pedido_compra(id_pedido_compra) ON UPDATE CASCADE ON DELETE CASCADE,
        CONSTRAINT fk_item_produto_pc FOREIGN KEY (id_produto) REFERENCES produto(id_produto) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    -- ==========================================================
    -- TABELA PEDIDO_VENDA
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS pedido_venda (
        id_pedido_venda SERIAL PRIMARY KEY,
        numero_pedido VARCHAR(20) NOT NULL UNIQUE,
        data_venda DATE DEFAULT CURRENT_DATE,
        valor_total NUMERIC(14,2) DEFAULT 0 CHECK (valor_total >= 0),
        desconto NUMERIC(12,2) DEFAULT 0 CHECK (desconto >= 0),
        forma_pagamento VARCHAR(50),
        status VARCHAR(30) DEFAULT 'ABERTO' CHECK (status IN ('ABERTO', 'FATURADO', 'FINALIZADO', 'CANCELADO')),
        observacoes TEXT,
        id_cliente INTEGER NOT NULL,
        id_funcionario INTEGER NOT NULL,
        CONSTRAINT fk_pv_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) ON UPDATE CASCADE ON DELETE RESTRICT,
        CONSTRAINT fk_pv_funcionario FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    -- ==========================================================
    -- TABELA ITEM_PEDIDO_VENDA
    -- ==========================================================
    CREATE TABLE IF NOT EXISTS item_pedido_venda (
        id_item_venda SERIAL PRIMARY KEY,
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        valor_unitario NUMERIC(12,2) NOT NULL CHECK (valor_unitario >= 0),
        desconto NUMERIC(12,2) DEFAULT 0 CHECK (desconto >= 0),
        subtotal NUMERIC(14,2) NOT NULL CHECK (subtotal >= 0),
        id_pedido_venda INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        CONSTRAINT fk_item_pv FOREIGN KEY (id_pedido_venda) REFERENCES pedido_venda(id_pedido_venda) ON UPDATE CASCADE ON DELETE CASCADE,
        CONSTRAINT fk_item_produto_pv FOREIGN KEY (id_produto) REFERENCES produto(id_produto) ON UPDATE CASCADE ON DELETE RESTRICT
    );
    """

    try:
        print("Iniciando a criação das tabelas no banco de dados...")

        # Instancia a sua classe de conexão que já pega os dados do .env
        banco = Conexao()

        # Executa o script de uma vez
        banco.cursor.execute(script_sql)

        # O commit é OBRIGATÓRIO, senão as tabelas são apagadas ao fechar a conexão
        banco.commit()

        print("Sucesso! Todas as tabelas foram criadas no banco de dados do Docker.")

    except Exception as e:
        print(f"\nErro ao criar as tabelas: {e}")
        if 'banco' in locals():
            banco.rollback()

    finally:
        # Fecha a conexão para não deixar conexões presas no PostgreSQL
        if 'banco' in locals():
            banco.fechar()
            print("Conexão com o banco encerrada.")


if __name__ == "__main__":
    criar_tabelas()