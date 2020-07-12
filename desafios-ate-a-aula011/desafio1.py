num = input('Digite um número inteiro: ')

if not num.isdigit():
    print('A entrada não é um número inteiro.')

else:
    num = int(num)

    if (num % 2 == 0):
        print(f'O número {num} é par.')

    elif (num % 2 == 1):
        print(f'O número {num} é ímpar.')
