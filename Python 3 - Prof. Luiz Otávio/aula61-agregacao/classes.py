from functools import reduce


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somar_valores(self):
        return reduce(lambda acumulado, proximo: acumulado + proximo.valor, self.produtos, 0)


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor