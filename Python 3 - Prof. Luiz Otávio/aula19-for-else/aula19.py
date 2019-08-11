"""
for / else
"""

lista = ['Luiz Otávio', 'Joãozinho', 'Maria']
comeca_com_j = False

for nome in lista:

    if nome.lower().startswith('j'):
        comeca_com_j = True
        continue

    print(nome)

else:
    if comeca_com_j:
        print('Existe uma palavra que começa com J')
    else:
        print('Não existe uma palavra que começa com J')
