"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Luiz otávio MIraNadA'
print(f'{nome:s}')
print(f'{nome.lower()}')  # Minúsculas
print(f'{nome.upper()}')  # Maiúsculas
print(f'{nome.title()}')  # Camel Case

num_1 = 1
# Coloca num_1 à direita e preenche com '-' a esquerda para completar tamanho 10
print(f'{num_1:->10}')
print(f'{num_1:-<10}')
print(f'{num_1:-^10}')
print(f'{num_1:-^10.2f}')
print('{n:@<20}'.format(n=num_1))
