class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando, classe: {self.nomeclasse}')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando, classe: {self.nomeclasse}')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando, classe: {self.nomeclasse}')
