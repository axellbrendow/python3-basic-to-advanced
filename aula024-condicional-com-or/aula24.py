"""
Expressões condicional com OR
"""

nome = input('Qual o seu nome ? ')

print(nome or None or False or 0 or 'Você não digitou nada.')

print('###############')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)
