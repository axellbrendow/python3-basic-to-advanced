from eletronico import Eletronico
from logmixin import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if (not self.ligado):
            print(f'{self._nome} não está ligado')
            self.log_error(f'{self._nome} não está ligado')

        elif (self._conectado):
            print(f'{self._nome} já está conectado')
            self.log_info(f'{self._nome} já está conectado')

        else:
            self._conectado = True
            print(f'{self._nome} foi conectado')

    def desconectar(self):
        if (not self.ligado):
            print(f'{self._nome} não está ligado')
            self.log_error(f'{self._nome} não está ligado')

        elif (not self._conectado):
            print(f'{self._nome} já está desconectado')
            self.log_info(f'{self._nome} já está desconectado')

        else:
            self._conectado = False
            print(f'{self._nome} foi desconectado')
