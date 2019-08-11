"""
for in
Iterando strings com for
Função range(start = 0, stop, step = 1)
"""

for i in range(10):
    print(i)

for i in range(20, 10, -1):
    print(i)

texto = 'Python'
novo_texto = ''

for n, letra in enumerate(texto):
    print(n, letra)

    if letra == 't':
        novo_texto = novo_texto + letra.upper()
    elif letra == 'h':
        novo_texto += letra.upper()
        break
    else:
        novo_texto += letra

print(novo_texto)
