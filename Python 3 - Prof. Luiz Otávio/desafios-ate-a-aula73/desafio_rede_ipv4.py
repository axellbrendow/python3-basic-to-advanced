""""
Lembrando que um ip é composto pela rede e pelo host. Além disso, um ip é uma sequência de bits.
"""

ip = '10.20.12.45'  # 00001010 00010100 00001100 00101101
mascara_subrede = '/26'  # Indica que os primeiros 26 bits do ip (da esquerda para direita) são da rede
# Ex.: /26 = 11111111 11111111 11111111 11000000 (255.255.255.192)
num_hosts = 2 ** 6 - 2  # 6 = número de zeros na máscara
rede_ip = '10.20.12.0'  # 1º ip da rede 00001010 00010100 00001100 00000000
broadcast_ip = '10.20.12.63'  # último ip da rede 00001010 00010100 00001100 00111111
primeiro_ip = '10.20.12.1'  # 1º ip da rede 00001010 00010100 00001100 00000001
ultimo_ip = '10.20.12.62'  # último ip da rede 00001010 00010100 00001100 00111110

ipv4 = int(''.join([format(int(x), '08b') for x in ip.split('.')]))
num_bits_mascara = int(mascara_subrede.split('/')[1])
mascara = int(('1' * num_bits_mascara).ljust(32, '0'))


def obter_dados_rede(ipv4: str, mascara: str):
    """
    Obtém todos os dados de range de ip de uma rede.

    :param ipv4: Cada um dos octetos na forma binária. Ex.: '00001010.00010100.00001100.00101101'
    :param mascara: Cada um dos octetos na forma binária. Ex.: '11111111.11111111.11111111.11000000'

    :return: O ipv4, a máscara, o número de hosts, o ip da rede, o ip de broadcast,
    o primeiro ip e o último ip todos em números decimais.
    """

    num_zeros = mascara.count('0')
    num_hosts = 2 ** num_zeros - 2
    ipv4_dec = '.'.join([str(int(x, 2)) for x in ipv4.split('.')])
    mascara_dec = '.'.join([str(int(x, 2)) for x in mascara.split('.')])
    ipv4_num = int(ipv4.replace('.', ''))
    mascara_num = int(mascara.replace('.', ''))

    return ipv4_dec, mascara_dec, num_hosts
