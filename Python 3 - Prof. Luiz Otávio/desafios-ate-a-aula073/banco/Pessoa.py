class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando, classe: {self.nomeclasse}')

    def __str__(self):
        return f"{{'nome': {self.nome}, 'idade': {self.idade}}}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self == other
