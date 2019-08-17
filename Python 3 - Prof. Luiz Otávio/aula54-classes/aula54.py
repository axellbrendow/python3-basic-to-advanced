from pessoa import Pessoa

p1 = Pessoa('Luiz', 20)
p2 = Pessoa('Maria', 19)

p1.comer('maçã')
p1.comer('pera')
p1.parar_de_comer()
p1.parar_de_comer()
p1.comer('pera')
p1.parar_de_comer()
p1.falar('Python')
p1.falar('C++')
p1.parar_de_falar()
p1.falar('C++')

print(p1.ano_atual)
print(Pessoa.ano_atual)
print(p1.ano_de_nascimento())
