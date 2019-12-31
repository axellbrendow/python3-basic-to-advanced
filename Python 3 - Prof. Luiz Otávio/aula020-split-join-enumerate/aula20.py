"""
Split, Join, Enumerate
* Split - Divide objetos iteráveis
* Join - Juntar objetos iteráveis
* Enumerate - Enumerar objetos iteráveis
"""

mystring = 'O Brasil é o o o país do futebol, o Brasil é penta.'
lista1 = mystring.split(' ')  # Corta a frase pelos espaços
lista2 = mystring.split(',')

print(lista1)
print(lista2)

palavra = ''
contagem = 0
quantidade_de_vezes = 0
quantidade_maxima = 0

for valor in lista1:  # Percorre cada palavra

    quantidade_de_vezes = lista1.count(valor)

    if quantidade_de_vezes > quantidade_maxima:
        quantidade_maxima = quantidade_de_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({quantidade_maxima}x).')

print('####################')

print(','.join(lista1))  # Concatena os elementos da lista com ',' entre eles

print('####################')

for indice, valor in enumerate(lista1):

    print(indice, valor)

print('####################')

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for numero, valor in lista:

    print(numero, valor)
