from random import randint
from Models.device_model import Dispositivo

class SensorBPM(Dispositivo):
    def __init__(self, nome : str, numero : str):
        super().__init__(nome = nome)
        self.numero = numero
        self.__historico_bpm = []


    @property
    def numero(self) -> str:
        return self.__numero

    @numero.setter
    def numero(self, entrada: str) -> None:
        if not isinstance(entrada, str):
            raise TypeError("O número de emergência deve ser uma string")

        if not entrada or not entrada.strip():
            raise ValueError("O número de emergência não pode estar vazio.")

        entrada_limpa = entrada.strip()
        if len(entrada_limpa) < 8 or len(entrada_limpa) > 11:
            raise ValueError("O número deve ter entre 8 a 11 caracteres.")

        if not entrada_limpa.isdigit():
            raise ValueError("O número deve conter apenas digitos númericos")

        self.__numero = entrada.strip()

    @property
    def historico_bpm(self) -> list[int]:
        return self.__historico_bpm.copy()

    def __emitir_alerta(self, bpm : int) -> str:
        return f"Frequência cardíaca anormal - {bpm}bpm. Enviando alerta para {self.numero}"

    def ler_bpm(self) -> str | int:
        bpm = randint(40,130)
        self.__historico_bpm.append(bpm)
        if bpm < 60 or bpm > 105:
            return self.__emitir_alerta(bpm)
        return bpm

    def ultimo_registro(self) -> int:
        if not self.__historico_bpm:
            raise IndexError("Não há nenhum registro de frequência cardíaca.")
        ultimo_bpm = self.__historico_bpm[-1]
        return ultimo_bpm



