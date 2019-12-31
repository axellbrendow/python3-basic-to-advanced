from banco.Conta import Conta
from banco.Agencia import Agencia
from banco.Cliente import Cliente


class ContaCorrente(Conta):
    def __init__(self, agencia: Agencia, conta: int, cliente: Cliente, saldo: float, limite: int = 100):
        super().__init__(agencia, conta, cliente, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')

        else:
            self.saldo -= valor
            print(f'Você sacou {valor} reais')
            self.detalhes()
