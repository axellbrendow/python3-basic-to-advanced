# https://rszalski.github.io/magicmethods/


class A:
    def __new__(cls, *args, **kwargs):

        # Padrão de projeto singleton, onde só é permitido criar uma instância da classe
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou o __init__')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        print(f'{{"{key}", "{value}"}}')
        self.__dict__[key] = value

    def __del__(self):
        print('Objeto coletado')

    def __str__(self):
        return 'Esta é a classe A'

    def __len__(self):
        return 55


a = A()
b = A()
c = A()

print(type(a))
print(a == b)
print(id(a))
print(id(b))
print(id(c))

a(1, 2, 3, 4, 5, nome='Luiz')
a.maluco = 'doido'
print(a.maluco)

print(a)
print(len(a))
