num = input('Informe o seu primeiro nome: ')

if (len(num) <= 4):
    print('Seu nome é curto.')

elif (len(num) <= 6):
    print('Seu nome é normal.')

else:
    print('Seu nome é muito grande.')
