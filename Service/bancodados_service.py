import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv

from Models.device_model import Dispositivo
from Models.usuario_model import Usuario

raiz = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=raiz / ".env")
caminho_db = os.getenv("CAMINHO_BANCO")

def abrir_conexao():
    return sqlite3.connect(caminho_db)

def salva_usuario(usuario : Usuario) -> None:
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

def salva_dispositivo(dispositivo : Dispositivo) -> None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = """INSERT INTO dispositivos (id, nome, status, criado_em) VALUES (?,?,?,?)"""
        valores = (f"{dispositivo.identidade}", dispositivo.nome, dispositivo.status, f"{dispositivo.criado_em}")

        cursor.execute(comando, valores)

def busca_dispositivo(id_dispositivo) -> Dispositivo | None:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM dispositivos WHERE id = (?)"
        valor = (str(id_dispositivo),)

        cursor.execute(comando, valor)

        resposta = cursor.fetchone()
        if resposta is None:
            return None
        return Dispositivo(resposta[0], resposta[2], resposta[3], resposta[4], resposta[1])

def lista_usuarios() -> list:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM usuarios"
        cursor.execute(comando)
        resposta = cursor.fetchall()

        usuarios = []
        for usuario in resposta:
            objeto_usuario = Usuario(usuario[0], usuario[1], usuario[2])
            usuarios.append(objeto_usuario)

        return usuarios

def lista_dispositivos() -> list:
    with abrir_conexao() as conexao:
        cursor = conexao.cursor()

        comando = "SELECT * FROM dispositivos"
        cursor.execute(comando)
        resposta = cursor.fetchall()

        dispositivos = []
        for dispositivo in resposta:
            d = Dispositivo(dispositivo[0], dispositivo[2], dispositivo[3], dispositivo[4], dispositivo[1])
            dispositivos.append(d)

        return dispositivos
