from random import uniform
from Models.device_model import Dispositivo

class SensorTemperatura(Dispositivo):
    def __init__(self, nome : str):
        super().__init__(nome)
        self.__historico_temperaturas = []

    @property
    def historico_temperaturas(self) -> list:
        return self.__historico_temperaturas.copy()

    def ultima_temperatura(self) -> float:
        if not self.__historico_temperaturas:
            raise IndexError("Não há nenhum registro no histórico de temperaturas")
        ultima_temperatura = self.__historico_temperaturas[-1]
        return ultima_temperatura

    def ler_temperatura(self) -> float:
        temperatura_atual = uniform(0,35)
        self.__historico_temperaturas.append(temperatura_atual)
        return temperatura_atual

