"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Luiz'
idade = 32
altura = 1.80
maior_de_idade = idade > 18
peso = 80
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior de idade:', maior_de_idade)

print(idade * altura)
print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc)
