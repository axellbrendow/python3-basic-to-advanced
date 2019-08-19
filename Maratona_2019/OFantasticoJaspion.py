
def traduzir(palavra_em_japones: str, dicionario: dict):
    traducao = dicionario.get(palavra_em_japones)  # None caso não haja a palavra no dicionário
    return palavra_em_japones if not traducao else traducao

numero_de_instancias = int(input())

for i in range(numero_de_instancias):
    numero_de_pares, numero_de_linhas_musica = [int(x) for x in input().split()]
    dicionario = dict()

    for j in range(numero_de_pares):
        palavra_em_japones = input()
        traducao_em_portugues = input()
        dicionario.update({palavra_em_japones: traducao_em_portugues})

    for k in range(numero_de_linhas_musica):
        palavras_musica = input().split()
        iterador = palavras_musica.__iter__()
        palavra = next(iterador)
        print(traduzir(palavra, dicionario), end='')

        for palavra in iterador:
            print(f' {traduzir(palavra, dicionario)}', end='')
        print()
