from itertools import combinations


def obter_palindromos(palavra):
    tamanho_palavra = len(palavra)
    palindromos = set()

    for i in range(tamanho_palavra):
        for group in combinations(palavra, i + 1):  # Combina em grupos de i + 1 elementos
            if group == group[::-1]:  # Checa se o grupo é igual ao inverso dele
                palindromos.add(group)

    return palindromos


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
