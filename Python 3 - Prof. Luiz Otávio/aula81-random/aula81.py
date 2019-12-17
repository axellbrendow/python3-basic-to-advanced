import random
import string

inteiro = random.randint(10, 20)
flutuante = random.uniform(10, 20)
inteirorange = random.randrange(10, 20, 2)

print(inteiro, flutuante, inteirorange)

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteado = random.choice(lista)
print(sorteado)

sorteados = random.choices(lista, k=2)  # Escolhe dois itens aleatórios (possível repetir)
print(sorteados)

sorteados_sem_rep = random.sample(lista, k=2)  # Escolhe dois itens aleatórios (possível repetir)
print(sorteados_sem_rep)

random.shuffle(lista)  # Embaralha a lista
print(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
especiais = '!@#$%&*._-'
geral = letras + digitos + especiais
senha = ''.join(random.choices(geral, k=20))

print(senha)
