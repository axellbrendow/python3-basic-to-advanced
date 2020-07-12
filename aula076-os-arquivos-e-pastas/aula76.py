import os

# ../../__file__
# caminho = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# termo = 'desafio'
caminho = input('Digite um caminho: ')
termo = input('Digite um termo: ')
contagem = 0
print()


def formata_tamanho(tamanho):
    base = 1024
    kilo = base ** 1
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        nome = 'B'

    elif tamanho < mega:
        nome = 'K'
        tamanho /= kilo

    elif tamanho < giga:
        nome = 'M'
        tamanho /= mega

    elif tamanho < tera:
        nome = 'G'
        tamanho /= giga

    elif tamanho < peta:
        nome = 'T'
        tamanho /= tera

    else:
        nome = 'P'
        tamanho /= peta

    return f'{round(tamanho, 2)}{nome}'.replace('.', ',')


for caminho_diretorio, diretorios, arquivos in os.walk(caminho):
    # print(caminho_diretorio)

    for arquivo in arquivos:
        if termo in arquivo:
            contagem += 1

            try:
                caminho_completo = os.path.join(caminho_diretorio, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', formata_tamanho(tamanho))
                print()

            except PermissionError as e:
                print('Sem permissões')

            except FileNotFoundError as e:
                print('Arquivo não encontrado')

            except Exception as e:
                print('Erro desconhecido.', e)

    # print(diretorios)
    # print(arquivos)
    # print()

print(f'{contagem} arquivo(s) encontrado(s)')
