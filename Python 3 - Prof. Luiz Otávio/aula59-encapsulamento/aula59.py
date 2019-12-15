"""
_ private/protected (public with an underscore _)
__ super private (can be acessed with _CLASSNAME__PROPERTY)
"""


class BadeDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BadeDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apagar_cliente(2)
bd.listar_clientes()
