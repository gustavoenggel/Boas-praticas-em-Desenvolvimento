create database projetoindustrial;
use projetoindustrial;
-- 1. Cria o banco de dados se ele não existir

-- 2. Cria a tabela de setores primeiro (pois o funcionário depende dela)
CREATE TABLE setor (
    id_setor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

-- 3. Cria a tabela de funcionários com a chave estrangeira (FK)
CREATE TABLE funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    id_setor INT NOT NULL,
    FOREIGN KEY (id_setor) REFERENCES setor(id_setor) ON DELETE CASCADE
);

-- 4. Insere os setores necessários
INSERT INTO setor (nome) VALUES 
('Usinagem'),
('Soldagem'),
('Qualidade');

-- 5. Insere os funcionários associando com o ID correto de cada setor
INSERT INTO funcionario (nome, cargo, id_setor) VALUES 
('Carlos Henrique', 'Operador CNC', 1),        -- 1 é Usinagem
('Marcos Paulo', 'Soldador Industrial', 2),   -- 2 é Soldagem
('Fernanda Lima', 'Inspetora de Qualidade', 3); -- 3 é Qualidade