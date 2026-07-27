from Service.bancodados_service import *

class GerenciadorDispositivos:
    @staticmethod
    def dispositivos_registrados() -> list:
        return lista_dispositivos()

    @staticmethod
    def usuarios_registrados() -> list:
        return lista_usuarios()

    @staticmethod
    def registrar_dispositivo(dispositivo : Dispositivo) -> None:
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Adicione um objeto do tipo 'Dispositivo'")
        if busca_dispositivo(dispositivo.identidade) is not None:
            raise ValueError("Dispositivo já existe")

        salva_dispositivo(dispositivo)
        return None

    @staticmethod
    def registrar_usuario(usuario : Usuario) -> None:
        if not isinstance(usuario, Usuario):
            raise TypeError("Adicione um objeto do tipo 'Usuário'")
        if busca_usuario(usuario.identidade) is not None:
            raise ValueError("Usuário já existe")

        salva_usuario(usuario= usuario)
        return None

    @staticmethod
    def buscar_usuario(id_usuario) -> Usuario | None:
        resposta = busca_usuario(id_usuario)
        return resposta

    @staticmethod
    def buscar_dispositivo(id_dispositivo) -> Dispositivo | None:
        resposta = busca_dispositivo(id_dispositivo)
        return resposta

    @staticmethod
    def remover_usuario(id_usuario) -> None:
        resposta = remove_usuario(id_usuario)
        if not resposta:
            raise ValueError("ID de usuário não registrado no banco de dados.")

        return None

    def associar_dispositivo(self, id_usuario, id_dispositivo) -> None:
        usuario = self.buscar_usuario(id_usuario)
        dispositivo = self.buscar_dispositivo(id_dispositivo)
        if usuario is None:
            raise ValueError("ID de usuário não registrado no banco de dados.")
        if dispositivo is None:
            raise ValueError("ID de dispositivo não registrado no banco de dados.")

        associa_dispositivo(id_usuario, id_dispositivo) #associa no banco de dados
        return None

    def desassociar_dispositivo(self, id_dispositivo) -> None:
        dispositivo = self.buscar_dispositivo(id_dispositivo)

        if dispositivo is None:
            raise ValueError("ID de dispositivo não registrado no banco de dados.")

        desassocia_dispositivo(id_dispositivo)
        return None
