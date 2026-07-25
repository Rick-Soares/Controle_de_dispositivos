import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv
from Models.usuario_model import Usuario

raiz = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=raiz / ".env")
caminho_db = os.getenv("CAMINHO_BANCO")

def abrir_conexao():
    return sqlite3.connect(caminho_db)

def salva_usuario(usuario : Usuario):
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "INSERT INTO usuarios (id, nome, email) VALUES (?,?,?)"
        valores = (str(usuario.identidade), usuario.nome, usuario.email)

        cursor.execute(comando, valores)

def busca_usuario(id_usuario) -> Usuario | None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM usuarios WHERE id = (?)"
        valor = (str(id_usuario),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchone()
        if resposta is None:
            return None
        return Usuario(resposta[0], resposta[1], resposta[2])

def remove_usuario(id_usuario) -> bool:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "DELETE FROM usuarios WHERE id = (?)"
        valor = (str(id_usuario),)

        cursor.execute(comando, valor)

        afetados = cursor.rowcount

        if afetados == 0:
            return False

        return True