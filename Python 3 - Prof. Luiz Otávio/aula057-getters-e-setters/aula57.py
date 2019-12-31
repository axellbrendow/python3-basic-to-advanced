
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    # Getter
    @property
    def nome(self):
        return self._nome  # O nome com underline é apenas uma convenção. Poderia ser outro.

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # Checa se valor é uma string
            valor = float(valor.replace('R$', ''))
        
        self._preco = valor


# p1 = Produto('CAMISETA', 50)
# p1.desconto(10)
# print(p1.nome, p1.preco)

# p2 = Produto('CANETA', 'R$15')
# p2.desconto(10)
# print(p2.nome, p2.preco)

class test:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('Get called')
        return self.value

    def __set__(self, instance, value):
        print('Set called for', value)
        self.value = value

class descripted:
    value = test(77)

d = descripted()
print(d.value)
d.value = 108
print(d.value)

# https://rszalski.github.io/magicmethods/
