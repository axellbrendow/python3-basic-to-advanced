num = input('Digite a hora atual: ')

if not num.isdigit():
    print('A entrada não é um número inteiro.')

else:
    num = int(num) % 24

    if (num < 12):
        print('Bom dia.')

    elif (num < 18):
        print('Boa tarde.')

    else:
        print('Boa noite.')
