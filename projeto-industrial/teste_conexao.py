from database import conectar

conexao = conectar()
if conexao.is_connected():
    print("conectado com sucesso!!")