def obter_indices_do_diamante(entrada: str):
    indice_abertura = -1
    indice_fechamento = -1

    for indice, caractere in enumerate(entrada):
        if caractere == '<':
            indice_abertura = indice

        elif caractere == '>' and indice_abertura > -1:
            indice_fechamento = indice
            break

    return indice_abertura, indice_fechamento


quantidade_de_entradas = int(input())

for i in range(quantidade_de_entradas):
    entrada = input()
    numero_de_diamantes = 0
    indice_abertura, indice_fechamento = obter_indices_do_diamante(entrada)

    while indice_abertura != -1 and indice_fechamento != -1:
        numero_de_diamantes += 1
        entrada = entrada[0:indice_abertura] + entrada[indice_fechamento + 1:]
        indice_abertura, indice_fechamento = obter_indices_do_diamante(entrada)

    print(numero_de_diamantes)
