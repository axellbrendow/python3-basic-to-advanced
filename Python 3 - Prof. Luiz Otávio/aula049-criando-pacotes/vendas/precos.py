from vendas.formatador import precos


def aumentar(valor, porcentagem, formatar=False):
    resultado = valor + valor * (porcentagem / 100)
    return resultado if not formatar else precos.formatar(resultado)


def reduzir(valor, porcentagem, formatar=False):
    return aumentar(valor, -porcentagem, formatar)
