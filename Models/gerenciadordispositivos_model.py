from Models.device_model import Dispositivo
from Models.usuario_model import Usuario


class GerenciadorDispositivos:
    def __init__(self):
        self.__dispositivos_registrados : list[Dispositivo]= []
        self.__usuarios_registrados : list[Usuario] = []

    @property
    def dispositivos_registrados(self) -> list:
        return self.__dispositivos_registrados.copy()

    @property
    def usuarios_registrados(self) -> list:
        return self.__usuarios_registrados.copy()

    def registrar_dispositivo(self, dispositivo : Dispositivo) -> None:
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Adicione um objeto do tipo 'Dispositivo'")

        if dispositivo in self.__dispositivos_registrados:
            raise ValueError("Esse dispositivo já foi registrado")
        self.__dispositivos_registrados.append(dispositivo)
        return None

    def registrar_usuario(self, usuario : Usuario) -> None:
        if not isinstance(usuario, Usuario):
            raise TypeError("Adicione um objeto do tipo 'Usuario'")

        if usuario in self.__usuarios_registrados:
            raise ValueError("Esse usuário já foi registrado")
        self.__usuarios_registrados.append(usuario)
        return None

    def buscar_usuario(self, id_usuario) -> Usuario:
        if not self.__usuarios_registrados:
            raise ValueError("Não há usuarios registrados")

        for u in self.__usuarios_registrados:
            if u.identidade == id_usuario:
                return u
        raise ValueError("Usuario não encontrado.")

    def buscar_dispositivo(self, id_dispositivo) -> Dispositivo:
        if not self.__dispositivos_registrados:
            raise ValueError("Não há dispositivos registrados")

        for d in self.__dispositivos_registrados:
            if d.identidade == id_dispositivo:
                return d
        raise ValueError("Dispositivo não encontrado.")

    def remover_usuario(self, id_usuario) -> tuple[bool, str]:
        usuario = self.buscar_usuario(id_usuario)

        self.__usuarios_registrados.remove(usuario)
        return True, "Usuario removido"

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
