import sys
import os

argumentos = sys.argv
quantidade_args = len(argumentos)

print(argumentos)

if quantidade_args <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')

else:
    mostrar_diretorios = '-d' in argumentos
    mostrar_arquivos = '-a' in argumentos

    if mostrar_diretorios:
        for arquivo in os.listdir('.'):
            if os.path.isdir(arquivo):
                print(arquivo)

    if mostrar_arquivos:
        for arquivo in os.listdir('.'):
            if os.path.isfile(arquivo):
                print(arquivo)
