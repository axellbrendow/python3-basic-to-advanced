class Meta(type):
    def __new__(metaclasse, nome, superclasses, namespace):
        if nome == 'A':
            return type.__new__(metaclasse, nome, superclasses, namespace)

        if 'attr_classe' in namespace:
            print(f'Removendo o atributo attr_classe da classe {nome}')
            del namespace['attr_classe']

        if 'b_fala' not in namespace:
            print(f'A classe {nome} precisa ter o método b_fala')

        elif not callable(namespace['b_fala']):
            print(f"{nome}()['b_fala'] deve ser um método")

        return type.__new__(metaclasse, nome, superclasses, namespace)


class A(metaclass=Meta):  # A própria classe A e suas filhas deveram atendar à metaclasse
    attr_classe = 'Valor A'
    pass


class B(A):
    attr_classe = 'Valor B'
    b_fala = 'wtf'

    def falar(self):
        print('B está falando')

    pass


class C(B):
    attr_classe = 'Valor C'
    pass


b = B()
print(b.attr_classe)

print()
c = C()
print(c.attr_classe)

print()
print('Criando uma classe pela classe type')

Pai = type('Pai', (), {'nome': 'Classe Pai'})
A = type('A', (Pai,), {'attr': 'Valor A'})

# Instancia a classe A
a = A()
print(a.attr)
print(a.nome)
