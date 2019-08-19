# { 'a': 'A',
#   'b': 'B',
#   'c': 'C',
#   'd': 'D',
#   'e': 'E',
#   'f': 'F',
#   'g': 'G',
#   'h': 'H',
#   'i': 'I',
#   'j': 'J',
#   'k': 'K',
#   'l': 'L',
#   'm': 'M',
#   'n': 'N',
#   'o': 'O',
#   'p': 'P',
#   'q': 'Q',
#   'r': 'R',
#   's': 'S',
#   't': 'T',
#   'u': 'U',
#   'v': 'V',
#   'w': 'W',
#   'x': 'X',
#   'y': 'Y',
#   'z': 'Z' }

minusculas = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' }

maiusculas = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' }

# maiuscula_para_minuscula =\
#     {maiuscula: minuscula for maiuscula, minuscula in zip(maiusculas, minusculas)}
#
# minuscula_para_maiuscula =\
#     {minuscula: maiuscula for minuscula, maiuscula in zip(minusculas, maiusculas)}

maiuscula_para_minuscula = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h',
    'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p',
    'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
    'Y': 'y', 'Z': 'z',
}

minuscula_para_maiuscula = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
    'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
    'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
    'y': 'Y', 'z': 'Z',
}

status = None


def minuscula(letra: str):
    global status

    if maiusculas.issuperset(letra):
        letra = maiuscula_para_minuscula[letra]
        status = 'ultima_minuscula'

    elif minusculas.issuperset(letra):
        status = 'ultima_minuscula'

    return letra


def maiuscula(letra: str):
    global status

    if minusculas.issuperset(letra):
        letra = minuscula_para_maiuscula[letra]
        status = 'ultima_maiuscula'

    elif maiusculas.issuperset(letra):
        status = 'ultima_maiuscula'

    return letra


def fazer_dancar(letra: str):
    global status

    if status == 'ultima_maiuscula':
        letra = minuscula(letra)

    elif status == 'ultima_minuscula':
        letra = maiuscula(letra)

    elif not status:
        if maiusculas.issuperset(letra): status = 'ultima_maiuscula'
        elif minusculas.issuperset(letra): status = 'ultima_minuscula'

    return letra


try:
    while True:
        sentenca = input()
        nova_sentenca = ''.join([fazer_dancar(letra) for letra in sentenca])
        print(nova_sentenca)

except:
    pass
