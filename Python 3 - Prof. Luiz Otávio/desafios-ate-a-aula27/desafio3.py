"""
3 - Crie uma função que recebe 2 números. O primeiro é um valor e o segundo um percentual
(ex.: 10%). Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def aumento(num1, num2):
    return num1 * (100 + num2) / 100

print(aumento(20, 50))
