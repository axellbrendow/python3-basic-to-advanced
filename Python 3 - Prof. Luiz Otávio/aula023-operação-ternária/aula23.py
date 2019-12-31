"""
Operador ternário
"""

usuario_logado = False
msg = 'Usuário logado.' if usuario_logado else 'Usuário precisa logar.'

print(msg)

print('##################')

idade = input('Qual a sua idade ? ')

if not idade.isnumeric():
    print('Digite apenas algarismos.')

else:
    print('Pode acessar.') if idade >= 18 else print('Não pode acessar.')
