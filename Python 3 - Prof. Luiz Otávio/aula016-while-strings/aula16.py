"""
Iterando sobre strings
"""

while True:
    mystring = input('Digite uma frase: ')
    newstring = ''
    tamanho = len(mystring)

    print(mystring.count('a'))

    c = 0

    while c < tamanho:

        if mystring[c] == 'r':
            newstring += 'R'
        else:
            newstring += mystring[c]

        print(newstring)

        c += 1

    c = 0
    maximo_de_repeticoes = 0
    repeticoes_da_letra = 0
    letra = ''

    while c < tamanho:

        repeticoes_da_letra = mystring.count(mystring[c])

        # .strip() remove espaços, o and dá True caso mystring[c].strip() não gere uma string vazia
        if repeticoes_da_letra > maximo_de_repeticoes and mystring[c].strip():

            maximo_de_repeticoes = repeticoes_da_letra
            letra = mystring[c]

        c += 1

    print(f'A letra "{letra}" foi a que mais se repetiu. {maximo_de_repeticoes} vezes.')
