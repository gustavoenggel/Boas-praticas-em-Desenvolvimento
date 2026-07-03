CREATE DATABASE metalsul_industrial;
USE metalsul_industrial;
CREATE TABLE setor (

id_setor INT AUTO_INCREMENT PRIMARY KEY,

nome VARCHAR(100) NOT NULL,

localizacao VARCHAR(150) NOT NULL

);
CREATE TABLE funcionario (

id_funcionario INT AUTO_INCREMENT PRIMARY KEY,

nome VARCHAR(150) NOT NULL,

cpf CHAR(11) NOT NULL UNIQUE,

cargo VARCHAR(100) NOT NULL,

salario DECIMAL(10,2) NOT NULL,

data_admissao DATE NOT NULL,
id_setor INT NOT NULL,
CONSTRAINT fk_funcionario_setor

FOREIGN KEY (id_setor)

REFERENCES setor(id_setor)

);
CREATE TABLE categoria_produto (

id_categoria INT AUTO_INCREMENT PRIMARY KEY,

nome VARCHAR(100) NOT NULL,

descricao TEXT

);
CREATE TABLE fornecedor (

id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,

razao_social VARCHAR(150) NOT NULL,

cnpj CHAR(14) NOT NULL UNIQUE,

telefone VARCHAR(20),

cidade VARCHAR(100) NOT NULL

);
CREATE TABLE produto (

id_produto INT AUTO_INCREMENT PRIMARY KEY,

nome VARCHAR(150) NOT NULL,

descricao TEXT,

preco_fabricacao DECIMAL(10,2) NOT NULL,

quantidade_estoque INT NOT NULL DEFAULT 0,
id_categoria INT NOT NULL,

id_fornecedor INT NOT NULL,
CONSTRAINT fk_produto_categoria

FOREIGN KEY (id_categoria)

REFERENCES categoria_produto(id_categoria),
CONSTRAINT fk_produto_fornecedor

FOREIGN KEY (id_fornecedor)

REFERENCES fornecedor(id_fornecedor)

);
CREATE TABLE ordem_producao (

id_ordem INT AUTO_INCREMENT PRIMARY KEY,

data_producao DATE NOT NULL,

quantidade_produzida INT NOT NULL,

status_producao VARCHAR(50) NOT NULL,

tempo_estimado INT NOT NULL,

tempo_real INT,
id_produto INT NOT NULL,

id_funcionario INT NOT NULL,
CONSTRAINT fk_ordem_produto

FOREIGN KEY (id_produto)

REFERENCES produto(id_produto),
CONSTRAINT fk_ordem_funcionario

FOREIGN KEY (id_funcionario)

REFERENCES funcionario(id_funcionario)

);
CREATE TABLE controle_qualidade (

id_qualidade INT AUTO_INCREMENT PRIMARY KEY,

data_inspecao DATE NOT NULL,

resultado_inspecao VARCHAR(50) NOT NULL,

observacoes_tecnicas TEXT,
id_ordem INT NOT NULL,
CONSTRAINT fk_qualidade_ordem

FOREIGN KEY (id_ordem)

REFERENCES ordem_producao(id_ordem)

);
USE metalsul_industrial;


-- =====================================================

-- POPULAÇÃO DA TABELA SETOR

-- =====================================================


INSERT INTO setor (nome, localizacao)

VALUES

('Usinagem', 'Bloco A'),

('Soldagem', 'Bloco B'),

('Pintura', 'Bloco C'),

('Montagem', 'Bloco D'),

('Qualidade', 'Bloco E');


-- =====================================================

-- POPULAÇÃO DA TABELA FUNCIONARIO

-- =====================================================


INSERT INTO funcionario

(nome, cpf, cargo, salario, data_admissao, id_setor)

VALUES

('Carlos Henrique', '11111111111', 'Operador CNC', 4500.00, '2021-03-10', 1),
('Marcos Paulo', '22222222222', 'Soldador Industrial', 4200.00, '2020-07-15', 2),
('Fernanda Lima', '33333333333', 'Inspetora de Qualidade', 5000.00, '2019-11-20', 5),
('Juliana Alves', '44444444444', 'Pintora Industrial', 3900.00, '2022-01-05', 3),
('Ricardo Souza', '55555555555', 'Montador Mecânico', 4100.00, '2021-09-12', 4),
('Patricia Gomes', '66666666666', 'Supervisora de Produção', 7500.00, '2018-05-18', 1),
('Lucas Martins', '77777777777', 'Auxiliar de Produção', 2800.00, '2023-02-01', 4),
('Amanda Costa', '88888888888', 'Analista de Qualidade', 5200.00, '2020-12-09', 5);


-- =====================================================

-- POPULAÇÃO DA TABELA CATEGORIA_PRODUTO

-- =====================================================


INSERT INTO categoria_produto (nome, descricao)

VALUES

('Estruturas Metálicas', 'Peças estruturais industriais'),
('Parafusos', 'Fixadores metálicos industriais'),
('Componentes Hidráulicos', 'Componentes para sistemas hidráulicos'),
('Peças Automotivas', 'Componentes destinados ao setor automotivo');


-- =====================================================

-- POPULAÇÃO DA TABELA FORNECEDOR

-- =====================================================


INSERT INTO fornecedor

(razao_social, cnpj, telefone, cidade)

VALUES

('Aço Forte LTDA', '11111111000111', '(47)99999-1111', 'Joinville'),
('Metal Prime Industrial', '22222222000122', '(47)99999-2222', 'Blumenau'),
('Hydra Components', '33333333000133', '(47)99999-3333', 'Jaraguá do Sul'),
('AutoParts Brasil', '44444444000144', '(47)99999-4444', 'Curitiba'),
('Fixadores União', '55555555000155', '(47)99999-5555', 'São Paulo');


-- =====================================================

-- POPULAÇÃO DA TABELA PRODUTO

-- =====================================================


INSERT INTO produto

(nome, descricao, preco_fabricacao, quantidade_estoque,

id_categoria, id_fornecedor)

VALUES
('Chassi Industrial',

'Estrutura metálica para máquinas industriais',

2500.00,

15,

1,

1),
('Parafuso Sextavado M10',

'Parafuso industrial galvanizado',

2.50,

5000,

2,

5),
('Cilindro Hidráulico HX20',

'Cilindro hidráulico de alta pressão',

850.00,

40,

3,

3),
('Suporte Automotivo X',

'Peça automotiva reforçada',

120.00,

150,

4,

4),
('Base Metálica Industrial',

'Base estrutural para equipamentos',

980.00,

30,

1,

2),
('Parafuso Allen M8',

'Parafuso allen para montagem industrial',

1.80,

3500,

2,

5),
('Válvula Hidráulica V300',

'Válvula para sistemas hidráulicos',

430.00,

60,

3,

3),
('Estrutura Tubular ZX',

'Estrutura metálica tubular',

1750.00,

20,

1,

1);


-- =====================================================

-- POPULAÇÃO DA TABELA ORDEM_PRODUCAO

-- =====================================================


INSERT INTO ordem_producao

(data_producao,

quantidade_produzida,

status_producao,

tempo_estimado,

tempo_real,

id_produto,

id_funcionario)

VALUES
('2026-05-01',

10,

'Concluída',

480,

500,

1,

1),
('2026-05-01',

2000,

'Concluída',

240,

230,

2,

6),
('2026-05-02',

15,

'Concluída',

360,

390,

3,

1),
('2026-05-03',

50,

'Em andamento',

300,

NULL,

4,

5),
('2026-05-03',

12,

'Concluída',

420,

415,

5,

1),
('2026-05-04',

1500,

'Concluída',

180,

175,

6,

6),
('2026-05-04',

25,

'Pausada',

240,

NULL,

7,

5),
('2026-05-05',

8,

'Concluída',

600,

640,

8,

1);


-- =====================================================

-- POPULAÇÃO DA TABELA CONTROLE_QUALIDADE

-- =====================================================


INSERT INTO controle_qualidade

(data_inspecao,

resultado_inspecao,

observacoes_tecnicas,

id_ordem)

VALUES
('2026-05-01',

'Aprovado',

'Produto dentro das especificações',

1),
('2026-05-01',

'Aprovado',

'Lote aprovado sem inconformidades',

2),
('2026-05-02',

'Reprovado',

'Vazamento identificado no teste hidráulico',

3),
('2026-05-02',

'Aprovado',

'Correção realizada e item aprovado',

3),
('2026-05-03',

'Em análise',

'Aguardando medições finais',

4),
('2026-05-04',

'Aprovado',

'Qualidade aprovada conforme padrão ISO',

5),
('2026-05-04',

'Aprovado',

'Parafusos dentro da tolerância',

6),
('2026-05-05',

'Reprovado',

'Estrutura apresentou desalinhamento',

8);
