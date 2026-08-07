#conexao com banco de dados
#instalar o drive conector
#mysql-connector
#drive é um tradutor - python para mysql

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        #o drive tenta abrir uma conexao
        host= "localhost",
        user= "root",
        password= "root",
        database= "metalsul_industrial"
        )
    return conexao

