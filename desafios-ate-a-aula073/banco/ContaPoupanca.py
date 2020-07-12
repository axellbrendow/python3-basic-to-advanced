from banco.Conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')

        else:
            self.saldo -= valor
            print(f'Você sacou {valor} reais')
            self.detalhes()
