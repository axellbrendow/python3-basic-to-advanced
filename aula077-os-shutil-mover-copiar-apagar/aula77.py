import os
import shutil
import sys

# ../../__file__
# caminho_original = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_original = r'C:\Users\ADM-Leka\Downloads\PB_Weapons\gente2'
caminho_novo = r'C:\Users\ADM-Leka\Downloads\PB_Weapons\gente'

try:
    os.mkdir(caminho_novo)

except FileExistsError as e:
    print(f'O diretório {caminho_novo} já existe')


for caminho_diretorio, diretorios, arquivos in os.walk(caminho_original):
    print(caminho_diretorio)
    for arquivo in arquivos:
        caminho_antigo_arquivo = os.path.join(caminho_diretorio, arquivo)
        caminho_novo_arquivo = os.path.join(caminho_novo, arquivo)

        try:
            shutil.move(caminho_antigo_arquivo, caminho_novo_arquivo)
            print(f'O arquivo {arquivo} foi movido com sucesso!')

        except:
            print(f'Não foi possível mover o arquivo {arquivo}', file=sys.stderr)

        try:
            shutil.copy(caminho_novo_arquivo, caminho_antigo_arquivo)
            print(f'O arquivo {arquivo} foi copiado com sucesso!')

        except:
            print(f'Não foi possível copiar o arquivo {arquivo}', file=sys.stderr)

        try:
            os.remove(caminho_novo_arquivo)
            print(f'O arquivo {arquivo} foi removido com sucesso!')

        except:
            print(f'Não foi possível remover o arquivo {arquivo}', file=sys.stderr)
