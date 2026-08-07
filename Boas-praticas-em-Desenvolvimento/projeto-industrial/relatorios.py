from database import conectar

def relatorio_producao_por_setor():
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = """
        SELECT 
        s.nome as Setor,
        SUM(o.quantidade_produzida) as Total_Produzido
        FROM setor s
        JOIN funcionario f
            ON s.id_setor = f.id_setor
        JOIN ordem_producao o
            ON o.id_funcionario = f.id_funcionario
        group by s.nome
        order by total_produzido DESC
    """
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("\n====== Produção por Setor ======")
    for relatorio in dados:
        print(f"\n Setor: {relatorio[0]}")
        print(f"\n Total Produzido: {relatorio[1]}")
        print("-"*40)


    cursor.close()
    conexao.close()
