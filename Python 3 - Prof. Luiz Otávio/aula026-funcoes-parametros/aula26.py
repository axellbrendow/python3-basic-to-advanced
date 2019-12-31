"""
Funções - def
"""


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)

saudacao('Olá', 'Luiz Otávio')
saudacao(nome='Luiz Otávio', msg='Olá')
saudacao()


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()

print('returned:', variavel)
