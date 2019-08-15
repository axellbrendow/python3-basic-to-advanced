"""
Funções - def - *args, **kwargs
"""

lista = [1, 2, 3, 4, 5]

print(lista)
print(*lista, sep='-')  # O asterisco * desempacota a lista, *lista é igual a 1, 2, 3, 4, 5

print('####################')


# O * desempacota listas, já o ** desempacota dicionários
def func(*args, **kwargs):  # key word arguments (nome='Luiz')
    print(args)
    print(f'primeiro = {args[0]}, ultimo = {args[-1]}, tamanho = {len(args)}')
    print(kwargs)
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')
    print(nome or 'Sem nome', sobrenome or 'Sem sobrenome', idade or 'Sem idade')
    print('###################')


func(1, 2, 3, 4, 5, nome='Luiz')
func(1, 2, 3, 4, 5, nome='Luiz', sobrenome='Otávio')
func(1, 2, 3, 4, 5, nome='Luiz', sobrenome='Otávio', idade=32)
