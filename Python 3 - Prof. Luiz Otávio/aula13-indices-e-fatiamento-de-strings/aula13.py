"""
Manipulando strings
* String índices
* Fatiamento de strings [início:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

# positivos     [012345678]
texto       =   'Python s2'
# positivos    -[987654321]

print(texto[2:6])
print(texto[:6])  # Equivalente a [0:6]
print(texto[7:])  # Equivalente a [7:9]
print(texto[-1])  # Equivalente a [8]
print(texto[-9:-3])  # Equivalente a [0:6]
print(texto[:-1])  # Equivalente a [0:8] (exclui o último caractere)
print(texto[0::2])  # Equivalente a [0] + [2] + [4] + [6] + [8]
print(len(texto))  # Tamanho da string
