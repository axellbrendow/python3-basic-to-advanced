from itertools import combinations


def obter_palindromos(palavra):
    tamanho_palavra = len(palavra)

    # Essa sintaxe é a de set comprehension em Python. Aqui há duas nested comprehensions.
    return {group for i in range(tamanho_palavra)
            # Gera combinações da palavra com grupos de caracteres cada vez maiores
            for group in combinations(palavra, i + 1) if group == group[::-1]}


try:
    while True:
        numero_de_palavras = int(input())
        palindromos = None

        if numero_de_palavras > 0:
            palavra = input()
            palindromos = obter_palindromos(palavra)

            for i in range(1, numero_de_palavras):
                palavra = input()
                palindromos = palindromos & obter_palindromos(palavra)

        if palindromos:
            maior_palindromo = max(palindromos, key=lambda palindromo: len(palindromo))
            print(len(maior_palindromo))

        else:
            print(0)

except:
    pass
