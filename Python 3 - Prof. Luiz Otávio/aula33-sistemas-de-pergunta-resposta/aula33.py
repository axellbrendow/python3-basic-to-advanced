
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta-certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta-certa': 'c',
    },
}

acertos = 0

for chave_pergunta, informacoes in perguntas.items():
    print(f'\n{chave_pergunta}: {informacoes["pergunta"]} ')
    print('Respostas:')

    for alternativa, valor in informacoes['respostas'].items():
        print(f'{alternativa}: {valor}')

    resposta = input('Sua resposta: ')

    if resposta == informacoes['resposta-certa']:
        acertos += 1
        print('Parabéns, você acertou !')
    
    else:
        print('EROOOUU !')

porcentagem = acertos / len(perguntas) * 100

print(f'\nQuantidade de acertos: {acertos}')
print(f'Sua porcentagem de acerto foi {porcentagem}%')
