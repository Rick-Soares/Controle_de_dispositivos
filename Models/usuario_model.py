from uuid import uuid4

from Models.device_model import Dispositivo

class Usuario:
    def __init__(self, id_usuario : str | None = None, nome : str = str, email : str = str):
        self.nome = nome
        self.email = email
        self.__dispositivos_salvos : list[Dispositivo] = []
        self.__identidade = id_usuario or uuid4()
    @property
    def identidade(self):
        return self.__identidade
    @property
    def nome(self) -> str:
        return self.__nome
    @property
    def email(self) -> str:
        return self.__email

    @nome.setter
    def nome(self, entrada):
        if not isinstance(entrada, str):
            raise TypeError("O nome deve ser uma string")

        entrada_limpa = entrada.strip()
        if not entrada_limpa:
            raise ValueError("O nome não pode estar vazio")

        self.__nome = entrada_limpa

    @email.setter
    def email(self, entrada):
        if not isinstance(entrada, str):
            raise TypeError("O email deve ser uma string")

        entrada_limpa = entrada.strip()
        if not entrada_limpa:
            raise ValueError("O email não pode estar vazio")

        if not entrada_limpa.endswith("@gmail.com"):
            raise ValueError("O email deve conter o dominio '@gmail.com'")
        self.__email = entrada_limpa

    @property
    def dispositivos_salvos(self) -> list[Dispositivo]:
        return self.__dispositivos_salvos.copy()

    def _salvar_dispositivo(self, dispositivo : Dispositivo) -> None:
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Insira um objeto do tipo Dispositivo")
        self.__dispositivos_salvos.append(dispositivo)
        return None

    def _remover_dispositivo(self, dispositivo : Dispositivo) -> None:
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Insira um objeto do tipo Dispositivo")
        self.__dispositivos_salvos.remove(dispositivo)
        return None

    def quantidade_dispositivos_salvos(self) -> int:
        return len(self.__dispositivos_salvos)
