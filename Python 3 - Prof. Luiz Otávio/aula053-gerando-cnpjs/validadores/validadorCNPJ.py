import itertools
import functools
import re


def remover_caracteres_especiais(cnpj):
    return re.sub('[^0-9]+', '', cnpj)
    # return cnpj.replace('.', '').replace('/', '').replace('-', '')


def ir_ate_2_comecando_de(valor_inicial):

    primeiro_gerador = (valor for valor in range(valor_inicial, 1, -1))
    segundo_gerador = (valor for valor in range(9, 1, -1))

    return itertools.chain(primeiro_gerador, segundo_gerador)  # Junta os dois

    # Outro código para essa função seria:
    #
    # for i in range(valor_inicial, 1, -1):
    #     yield i
    #
    # for i in range(9, 1, -1):
    #     yield i


def obter_iterador_cnpj_sequencia(cnpj):
    # Junta o iterador do CNPJ com o gerador da sequencia 5,.,.,2,9,.,.,.,.,.,.,2
    inicio_sequencia = 5 if len(cnpj) == 12 else 6
    iterador_cnpj = cnpj.__iter__()
    gerador_sequencia = ir_ate_2_comecando_de(inicio_sequencia)

    return zip(iterador_cnpj, gerador_sequencia)  # Junta os dois iteradores


def digito_verificador(cnpj):
    cnpj = remover_caracteres_especiais(cnpj)
    if cnpj[0] * len(cnpj) == cnpj or len(cnpj) != 12 and len(cnpj) != 13:
        raise ValueError(f'O CNPJ {cnpj} é inválido.')
    iterador_cnpj_sequencia = obter_iterador_cnpj_sequencia(cnpj)

    soma = functools.reduce(lambda acumulado, item_atual:
                     # item_atual[0] é o algarismo do CNPJ
                     # item_atual[1] é o valor da sequência 5,.,.,2,9,.,.,.,.,.,.,2
                     acumulado + int(item_atual[0]) * item_atual[1],
                     iterador_cnpj_sequencia, 0)

    formula = 11 - (soma % 11)
    digito = formula if formula < 10 else 0
    return str(digito)


def validar(cnpj):
    # Remove os dois últimos dígitos do cnpj
    cnpj1 = cnpj[:-2] + digito_verificador(cnpj[:-2])
    cnpj2 = cnpj1 + digito_verificador(cnpj1)
    return cnpj2 == cnpj
