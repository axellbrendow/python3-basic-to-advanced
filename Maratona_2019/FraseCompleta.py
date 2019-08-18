TAMANHO_ALFABETO = 26
numero_de_entradas = int(input())

for i in range(numero_de_entradas):
    frase = input()
    # A notação {c for c in frase} cria uma estrutura de dados do tipo Set em Python
    numero_de_letras = len({c for c in frase if 'a' <= c <= 'z'})

    if numero_de_letras >= TAMANHO_ALFABETO:
        print('frase completa')

    elif numero_de_letras >= TAMANHO_ALFABETO / 2:
        print('frase quase completa')

    else:
        print('frase mal elaborada')
