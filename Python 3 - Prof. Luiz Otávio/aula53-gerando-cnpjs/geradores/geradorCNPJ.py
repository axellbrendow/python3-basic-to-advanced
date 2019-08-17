import random

from validadores.validadorCNPJ import digito_verificador


def gerar():
    digito1 = random.randint(0, 9)
    digito2 = random.randint(0, 9)
    bloco2 = random.randint(100, 999)  # Número de 3 dígitos
    bloco3 = random.randint(100, 999)  # Número de 3 dígitos
    bloco4 = '0001'
    cnpj = f'{digito1}{digito2}.{bloco2}.{bloco3}/{bloco4}-'

    digito_verificador1 = digito_verificador(cnpj)
    cnpj += digito_verificador1

    digito_verificador2 = digito_verificador(cnpj)
    cnpj += digito_verificador2

    return cnpj
