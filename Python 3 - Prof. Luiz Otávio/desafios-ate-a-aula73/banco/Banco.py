from banco.Cliente import Cliente
from banco.Conta import Conta
from banco.ContaCorrente import ContaCorrente
from banco.ContaPoupanca import ContaPoupanca


class Banco:
    def __init__(self, clientes: list[Cliente], contas: list[Conta], agencias: list[int]):
        self.__clientes = clientes
        self.__contas = contas
        self.__agencias = agencias

    def adicionar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        if conta.agencia not in self.__agencias:
            print(f'A conta {conta} não pertence ao banco {self}')

        else:
            self.__contas.append(conta)

    def __str__(self):
        return f"{{'agencias': {self.__agencias}}}"
