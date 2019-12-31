# abc = Abstract Base Class
from abc import ABC, abstractmethod
from banco.Agencia import Agencia
from banco.Cliente import Cliente


class Conta(ABC):
    def __init__(self, agencia: Agencia, conta: int, cliente: Cliente, saldo: float):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._cliente = cliente

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')

        else:
            self._saldo = valor

    @property
    def cliente(self):
        return self._cliente

    def detalhes(self):
        # print(f'Cliente: {self.cliente}, Agência: {self.agencia}, Conta: {self.conta}, Saldo: {self.saldo}')
        # print(f'Detalhes: Cliente: {self.cliente}, Conta: {self.conta}, Saldo: {self.saldo}')
        print(f'Detalhes: Conta: {self.conta}, Saldo: {self.saldo}')

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico')

        else:
            self.saldo += valor
            print(f'Você depositou {valor} reais')
            self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

    def __str__(self):
        return f"{{'agencia': {self.agencia}, 'cliente': {self.cliente}, 'conta': {self.conta}, 'saldo': {self.saldo}}}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self == other
