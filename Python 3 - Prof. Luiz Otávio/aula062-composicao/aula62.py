from classes import Cliente

# Observar que, como os endereços estão associados por composição à classe Cliente,
# ao deletar um cliente, os endereços são deletados juntos.

c1 = Cliente('Luiz', 32)
c1.inserir_endereco('Belo Horizonte', 'MG')
print(c1.nome)
c1.listar_enderecos()
del c1
print()

c2 = Cliente('Maria', 55)
c2.inserir_endereco('Salvador', 'BA')
c2.inserir_endereco('Rio de Janeiro', 'RJ')
print(c2.nome)
c2.listar_enderecos()
print()

c3 = Cliente('João', 19)
c3.inserir_endereco('São Paulo', 'SP')
print(c3.nome)
c3.listar_enderecos()
print()

print('#########################################')
