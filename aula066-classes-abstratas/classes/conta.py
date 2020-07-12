from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

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

    def detalhes(self):
        print(f'Agência: {self.agencia}, Conta: {self.conta}, Saldo: {self.saldo}')

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
