"""
class Arquivo:
    def __init__(self, nomearquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(nomearquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        print('tb', exc_tb)
        print('type', exc_type)
        print('val', exc_val)

        # Ignora exceções que venham a ser levantadas.
        # return True pressupõe que você tratou as exceções
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.asdasd('Alguma coisa')
"""

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo

    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
