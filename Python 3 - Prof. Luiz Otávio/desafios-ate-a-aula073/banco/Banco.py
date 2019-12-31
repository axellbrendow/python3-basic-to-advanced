from typing import List, Union
from banco.Cliente import Cliente
from banco.Conta import Conta
from banco.Agencia import Agencia


class Banco:
    def __init__(self, nome: str, agencias: List[Agencia], clientes: List[Cliente], contas: List[Conta]):
        self.__nome = nome
        self.__agencias = []
        self.__clientes = []
        self.__contas = []

        for agencia in agencias: self.adicionar_agencia(agencia)
        for cliente in clientes: self.adicionar_cliente(cliente)
        for conta in contas: self.adicionar_conta(conta)

    @property
    def agencias(self):
        return self.__agencias

    @property
    def clientes(self):
        return self.__clientes

    @property
    def contas(self):
        return self.__contas

    def pertence_ao_banco(self, objeto: Union[Agencia, Cliente, Conta]):
        if isinstance(objeto, Agencia):
            return objeto.banco == self.__nome

        elif isinstance(objeto, Cliente):
            return objeto.agencia in self.__agencias

        elif isinstance(objeto, Conta):
            return objeto.agencia in self.__agencias

        else:
            print(f'O banco possui apenas Agências, Clientes e Contas. O objeto recebido é {objeto}.')
            return False

    def adicionar_agencia(self, agencia: Agencia):
        if not self.pertence_ao_banco(agencia):
            print(f'A agencia {agencia} não pertence ao banco {self}')

        else:
            self.__agencias.append(agencia)

    def adicionar_cliente(self, cliente: Cliente):
        if not self.pertence_ao_banco(cliente):
            print(f'O cliente {cliente} não pertence ao banco {self}')

        else:
            self.__clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        if not self.pertence_ao_banco(conta):
            print(f'A conta {conta} não pertence ao banco {self}')

        else:
            self.__contas.append(conta)

    def sacar(self, cliente: Cliente, conta: Conta, valor: float):
        if not self.pertence_ao_banco(cliente):
            print(f'O cliente {cliente} não pertence ao banco {self}')

        elif not self.pertence_ao_banco(conta):
            print(f'A conta {conta} não pertence ao banco {self}')

        elif conta.cliente != cliente:
            print(f'A conta {conta} não pertence ao cliente {cliente}')

        else:
            if cliente not in self.__clientes: self.adicionar_cliente(cliente)
            if conta not in self.__contas: self.adicionar_conta(conta)

            conta.sacar(valor)

    def __str__(self):
        return f"{{'nome': {self.__nome}}}"
