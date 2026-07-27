from Models.device_model import Dispositivo

class DetectorQueda(Dispositivo):
    def __init__(self, nome : str, numero : str):
        super().__init__(nome = nome)
        self.numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, entrada : str):
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

    def detectar_queda(self):
        if self.status == "Ativo":
            return True, f"Queda detectada! Ligando para {self.numero}"
        return False, "O dispositivo está inativo. Não é possivel detectar uma queda"

