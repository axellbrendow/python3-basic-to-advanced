# stack

livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livros, livro_removido)

# queue

from collections import deque

fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Luiz Otávio')
fila.append('Marcos')
fila.append('José')

print(fila)

print(f'Removendo {fila.popleft():12}... -> {fila}')
print(f'Removendo {fila.popleft():12}... -> {fila}')
print(f'Removendo {fila.popleft():12}... -> {fila}')
print(f'Removendo {fila.popleft():12}... -> {fila}')
print(f'Removendo {fila.popleft():12}... -> {fila}')


fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
print(fila)

fila.append(5)
print(fila)

fila.append(6)
print(fila)

from time import sleep

fila = deque(maxlen=10)

for i in range(1000):
    fila.append(i)
    sleep(0.01)
    print(f'\r{fila}', end='')
