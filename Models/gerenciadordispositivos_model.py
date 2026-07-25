from Models.device_model import Dispositivo
from Models.usuario_model import Usuario
from Service.bancodados_service import *

class GerenciadorDispositivos:
    def __init__(self):
        self.__dispositivos_registrados : list[Dispositivo]= []
        self.__usuarios_registrados : list[Usuario] = []

    @property
    def dispositivos_registrados(self) -> list:
        return lista_dispositivos()

    @property
    def usuarios_registrados(self) -> list:
        return lista_usuarios()

    def registrar_dispositivo(self, dispositivo : Dispositivo) -> None:
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Adicione um objeto do tipo 'Dispositivo'")
        if busca_dispositivo(dispositivo.identidade) is not None:
            raise ValueError("Dispositivo já existe")

        salva_dispositivo(dispositivo)
        return None

    def registrar_usuario(self, usuario : Usuario) -> None:
        if not isinstance(usuario, Usuario):
            raise TypeError("Adicione um objeto do tipo 'Usuário'")
        if busca_usuario(usuario.identidade) is not None:
            raise ValueError("Usuário já existe")

        salva_usuario(usuario= usuario)
        return None

    def buscar_usuario(self, id_usuario) -> Usuario | None:
        resposta = busca_usuario(id_usuario)
        return resposta

    def buscar_dispositivo(self, id_dispositivo) -> Dispositivo | None:
        resposta = busca_dispositivo(id_dispositivo)
        return resposta

    def remover_usuario(self, id_usuario) -> None:
        resposta = remove_usuario(id_usuario)
        if not resposta:
            raise ValueError("ID de usuário não registrado no banco de dados.")

        return None

    def associar_dispositivo(self, id_usuario, id_dispositivo) -> None:
        usuario = self.buscar_usuario(id_usuario)
        dispositivo = self.buscar_dispositivo(id_dispositivo)

        usuario._salvar_dispositivo(dispositivo)
        return None

    def desassociar_dispositivo(self, id_usuario, id_dispositivo) -> tuple[bool, str]:
        usuario = self.buscar_usuario(id_usuario)
        dispositivo = self.buscar_dispositivo(id_dispositivo)

        if dispositivo in usuario.dispositivos_salvos:
            usuario._remover_dispositivo(dispositivo)
            return True, "Dispositivo desassociado ao usuario"
        return False, "Dispositivo não está associado ao usuario"
