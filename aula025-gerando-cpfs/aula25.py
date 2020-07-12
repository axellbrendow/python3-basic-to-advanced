"""
Gerar CPFs aleatórios

CPF = 168.995.350-09
--------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 54           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
       + --           # -> 0 *  2 = 0
         297          #              343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
1º Dígito = 0         #   2º Dígito = 9
"""

from random import randint

numero = str(randint(10000000000, 99999999999))
cpf = numero
cpf_tratado = cpf.replace('.', '').replace('-', '')[:-2]  # Remove caracteres especiais
sum = 0
verificador1 = 0
verificador2 = 0

# Calculando o 1º dígito verificador
for i, value in enumerate(range(10, 1, -1)):

    sum += int(cpf_tratado[i]) * value

sum = 11 - (sum % 11)
verificador1 = 0 if sum > 9 else sum

cpf_tratado += str(verificador1)

# Calculando o 2º dígito verificador
sum = 0

for i, value in enumerate(range(11, 1, -1)):

    sum += int(cpf_tratado[i]) * value

sum = 11 - (sum % 11)
verificador2 = 0 if sum > 9 else sum

cpf_tratado += str(verificador2)
cpf_tratado = f'{cpf_tratado[0:3]}.{cpf_tratado[3:6]}.{cpf_tratado[6:9]}-{cpf_tratado[9:11]}'

print(cpf_tratado)
# print('Válido !' if cpf_tratado == cpf else 'Inválido !')
