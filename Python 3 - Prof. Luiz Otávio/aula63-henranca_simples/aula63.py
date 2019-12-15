from classes import Cliente, Aluno, Pessoa

# Observar que, como os endereços estão associados por composição à classe Cliente,
# ao deletar um cliente, os endereços são deletados juntos.

c1 = Cliente('Luiz', 32)
c1.falar()
c1.comprar()
print()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()
print()

p1 = Pessoa('João', 43)
p1.falar()
print()

print('#########################################')
