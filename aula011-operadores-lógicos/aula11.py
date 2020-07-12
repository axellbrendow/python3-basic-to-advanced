"""
Operadores lógicos
and, or, not
in e not in
"""

a = 2
b = 3

if b > a:
    print('if')
else:
    print('else')

if not b > a:
    print('if')
else:
    print('else')

a = ''

if not a:
    print('if')
else:
    print('else')

nome = 'Luiz Otávio'

if 'Otá' in nome:
    print('Existe a string no seu nome.')
else:
    print('Não existe a string no seu nome.')
