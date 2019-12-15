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

    def falar(self):
        print(f'{self.nome} está falando clientês, classe: {self.nomeclasse}')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()
        print(f'{self.nome} {self.sobrenome} está falando vipês, classe: {self.nomeclasse}')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando, classe: {self.nomeclasse}')
