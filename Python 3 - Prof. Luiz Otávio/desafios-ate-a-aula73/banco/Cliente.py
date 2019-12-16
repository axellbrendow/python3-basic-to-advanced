from banco.Pessoa import Pessoa


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando, classe: {self.nomeclasse}')
