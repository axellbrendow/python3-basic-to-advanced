"""
Listas
* Fatiamente
* append, insert, pop, del, clear, extend, min, max, range
"""

#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#     -   6    5    4    3    2    1

# Fatiamento
print(lista)
print(lista[5])
print(lista[:4])
print(lista[2:])
print(lista[::2])
print(lista[::-1])  # O -1 faz com que start e end sejam invertidos

print('#################')

# Fatiamento concatenação
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2

print(lista1)
print(lista2)
print(lista3)

print('#################')

# Inserção
lista2.extend(lista1)
lista1.append(4)
lista1.insert(0, 0)

print(lista1)
print(lista2)

print('#################')

# Remoção
lista1.pop()
print(lista1)

del(lista1[1:3])
print(lista1)

print('#################')

# Comparações
lista1.insert(0, 9)
print( max(lista1) )

print('#################')

# Cria uma lista a partir de um iterador
lista2 = list( range(1, 10) )  # Cria uma lista passando pelos elementos do iterador range()
print(lista2)

print('#################')

print('Jogo da forca')

palavra_secreta = 'perfume'
palavra_temporaria = ''
letra = ''
acertos = []
chances = 5

while chances > 0:
    print()
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Só é permitido um único caractere.')
        continue

    acertos.append(letra)

    if letra in palavra_secreta:
        print(f'Parabéns ! Você encontrou a letra "{letra}".')

    else:
        print(f'A letra "{letra}" não existe na palavra secreta.')
        acertos.pop()
        chances -= 1

    palavra_temporaria = ''

    for letra_secreta in palavra_secreta:

        if letra_secreta in acertos:
            palavra_temporaria += letra_secreta

        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra_secreta:
        print(f'Parabéns ! Você ganhou. A palavra era {palavra_secreta}.')
        break

    else:
        print(f'Status da palavra secreta: {palavra_temporaria}.')

    print(f'Você ainda tem {chances} chances.')

if chances < 1:
    print()
    print('Numero de chances esgotado.')
