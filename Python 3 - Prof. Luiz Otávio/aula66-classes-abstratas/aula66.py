# abc = abstract base class
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B')


b = B()
b.falar()

print('\nExemplo com contas bancárias:')

from classes.ContaPoupanca import ContaPoupanca
from classes.conta import Conta
from classes.ContaCorrente import ContaCorrente

print('\nConta Poupança')
cp = ContaPoupanca(1111, 2222, 0)
cp.detalhes()
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

# c = Conta(1111, 2222, 0)  # Erro. Conta é uma classe abstrata

print('\nConta Corrente')
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
