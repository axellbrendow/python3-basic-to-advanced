class A:
    def falar(self):
        print(f'Falando... Estou em A')


class B(A):
    def falar(self):
        print(f'Falando... Estou em B')


class C(A):
    def falar(self):
        print(f'Falando... Estou em C')


class D(B, C):  # Problema do diamante. D herda de duas classes com o mesmo método
    pass


d = D()
d.falar()


print('\nExemplo real de herança múltipla')

from smartphone import Smartphone

s1 = Smartphone('Pocophone F1')
s1.conectar()
s1.desligar()
s1.ligar()
s1.conectar()
s1.conectar()
s1.conectar()
s1.desligar()
s1.conectar()
s1.desconectar()
