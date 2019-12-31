from pessoa import Pessoa

p1 = Pessoa('Luiz', 20)
# p2 = Pessoa('Maria', 19)
p2 = Pessoa.criar_por_ano_de_nascimento('Maria', 2000)
print(p2)
print(p2.nome, p2.idade)
