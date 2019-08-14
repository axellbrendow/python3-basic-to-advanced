"""
Dictionary Comprehension
Set Comprehension
"""

l1 = [
    ('chave1', 2),
    ('chave2', 'valor2'),
]

d1 = {x: y * 2 for x, y in l1}

print(d1)

d2 = {x for x in range(5)}

print(d2, type(d2))

d3 = {f'chave_{x}': x**2 for x in range(5)}

print(d3, type(d3))
