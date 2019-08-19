from pessoa import Pessoa

p1 = Pessoa('Luiz', 20)
# p2 = Pessoa('Maria', 19)
p2 = Pessoa.criar_por_ano_de_nascimento('Maria', 2000)
print(p2)
print(p2.nome, p2.idade)

# p1.comer('maçã')
# p1.comer('pera')
# p1.parar_de_comer()
# p1.parar_de_comer()
# p1.comer('pera')
# p1.parar_de_comer()
# p1.falar('Python')
# p1.falar('C++')
# p1.parar_de_falar()
# p1.falar('C++')

# print(p1.ano_atual)  # O atributo ano_atual é da classe Pessoa e não do objeto
# print(Pessoa.ano_atual)  # É possível acessar diretamente o atributo da classe
# print(p1.ano_de_nascimento())
