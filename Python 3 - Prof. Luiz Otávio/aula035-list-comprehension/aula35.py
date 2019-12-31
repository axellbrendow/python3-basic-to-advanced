"""
List Comprehension

[expression for variable in list]
<expression> pode ou não usar <variable> dentro dela.
<expression>
"""

# l -> lista, ex -> exemplo
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [v for v in l1]  # Copia todos os elementos de l1 para ex1
ex2 = [v * 2 for v in l1]  # Copia os elementos multiplicando-os por 2
ex3 = [(v, v2) for v in l1 for v2 in range(2)]

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]

t1 = (
    ('c1', 'v1'),
    ('c2', 'v2'),
    ('c3', 'v3'),
)

ex5 = [(v, c) for c, v in t1]

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0 if v % 7 == 0]  # list Comprehension com IFs

print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex6)
