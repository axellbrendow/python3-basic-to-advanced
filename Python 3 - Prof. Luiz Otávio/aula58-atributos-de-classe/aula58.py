class A:
    vc = 123

    def __init__(self):
        self.vc = 321

a1 = A()
a2 = A()

a1.vc = 777  # Cria o atributo 'vc' em a1

# Ao acessar uma propriedade, o interpretador do Python busca
# ela primeiro na instância do objeto e depois na classe
print(a1.vc)
print(a2.vc)
print(A.vc)
