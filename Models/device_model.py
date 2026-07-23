from datetime import datetime, UTC
import uuid


class Dispositivo:
    def __init__(self, nome : str):
        self.nome = nome

        self.__bateria : float = 100
        self.__status : str = "Ativo"
        self.__criado_em : datetime = datetime.now(UTC)
        self.__identidade = uuid.uuid4()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, entrada : str):
        if not isinstance(entrada, str):
            raise TypeError("O nome deve ser uma string")

        if not entrada or not entrada.strip():
            raise ValueError("O nome não pode estar vazio")
        self.__nome = entrada.strip()

    def ativar(self) -> tuple[bool, str]:
        if self.__status == "Ativo":
            return False, "Dispositivo já está ativo"

        if self.__bateria > 0:
            self.__status = "Ativo"
            return True, "Dispositivo ativado"

        return False, "Não é possivel ativar o dispositivo (sem bateria)"

    def desativar(self) -> tuple[bool, str]:
        if self.__status == "Ativo":
            self.__status = "Inativo"
            return True, "Dispositivo desativado"
        return False, "Dispositivo já está desativado"

    def carregar(self, quantidade: float) -> tuple[bool, str]:
        if quantidade > 100 or quantidade < 0:
            raise ValueError("Quantidade invalida")

        if self.__bateria == 100:
            return False, "A bateria já está totalmente carregada."

        elif (self.__bateria + quantidade) >= 100:
            self.__bateria = 100
            return True, "Bateria foi 100% carregada."

        self.__bateria += quantidade
        return True, f"Bateria carregada até {self.__bateria}%"

    def descarregar(self, quantidade: float) -> tuple[bool, str]:
        if quantidade > 100 or quantidade < 0:
            raise ValueError("Quantidade invalida")

        if self.__status == "Ativo":
            if (self.__bateria - quantidade) <= 0:
                self.__status = "Inativo"
                self.__bateria = 0
                return True, "Dispositivo descarregado até 0%."
            self.__bateria -= quantidade
            return True, f"Dispositivo descarregado até {self.__bateria}%"

        return False, "Dispositivo está inativo"

    def __str__(self) -> str:
        return f"O dispositivo '{self.nome}' criado em {self.__criado_em} está {self.__status} e com {self.__bateria}%"

    @property
    def bateria(self) -> float:
        return self.__bateria

    @property
    def status(self) -> str:
        return self.__status
