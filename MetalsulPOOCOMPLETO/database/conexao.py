import os
import psycopg #postgre
from dotenv import load_dotenv

load_dotenv() #carrega automaticamente as variáveis existentes no .env

class Conexao:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT")
        self.conexao = psycopg.connect(
            host=self.host,
            dbname=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
            options="-c search_path=empresa"  # <-- Adicione esta linha
        )

        self.cursor = self.conexao.cursor()

    def commit(self):
        self.conexao.commit()
    def rollback(self):
        self.conexao.rollback()
    def fechar(self):
        self.conexao.close()
        self.cursor.close()