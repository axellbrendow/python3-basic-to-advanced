from zipfile import ZipFile
import os

caminho = 'C:\\Users\\ADM-Leka\\Downloads\\PB_Weapons\\PUC_-_Ciência_da_Computação\\CursosPython\\Python 3 - Prof. Luiz Otávio\\venv\\'

with ZipFile('venv.zip', 'w') as zipper:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zipper.write(caminho_completo, arquivo)
        print(caminho_completo, 'foi zipado !')

print('\nArquivos dentro do zip:')

with ZipFile('venv.zip', 'r') as zipper:
    for arquivo in zipper.namelist():
        print(arquivo)

with ZipFile('venv.zip', 'r') as zipper:
    zipper.extractall('venv_descompactado')
