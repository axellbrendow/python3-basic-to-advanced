"""
Somar os preços de produtos com List Comprehension
"""

# print(sum([valor for produto, valor in carrinho]))

import time

carrinho = []
carrinho.append(('Produto 1', 80))
carrinho.append(('Produto 2', 70))
carrinho.append(('Produto 3', 30))
carrinho.append(('Produto 4', 10))
carrinho.append(('Produto 5', 50))
carrinho.append(('Produto 6', 90))

################################## Benchmark

inicio = time.time()
for i in range(1000000):
    sum([valor for produto, valor in carrinho])

fim = time.time()

print(f'tempo = {fim - inicio}s')

################################## Benchmark

inicio = time.time()
for i in range(1000000):
    total = 0

    for j in range(len(carrinho)):
        total += carrinho[j][1]

fim = time.time()

print(f'tempo = {fim - inicio}s')
