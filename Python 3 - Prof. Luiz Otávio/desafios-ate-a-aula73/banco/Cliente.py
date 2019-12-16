from banco.Pessoa import Pessoa
from banco.Agencia import Agencia


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, agencia: Agencia):
        super().__init__(nome, idade)
        self.__agencia = agencia

    @property
    def agencia(self):
        return self.__agencia

    def __str__(self):
        return f"{{'nome': {self.nome}, 'idade': {self.idade}, 'agencia': {self.agencia}}}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self == other
