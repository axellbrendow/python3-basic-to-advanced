""""
Lembrando que um ip é composto pela rede e pelo host.
Além disso, um ip é uma sequência de bits.
"""

ip = '10.20.12.45'  # 00001010 00010100 00001100 00101101
mascara_subrede = '/26'  # Indica que os primeiros 26 bits do ip (da esquerda para direita) são da rede
# Ex.: /26 = 11111111 11111111 11111111 11000000 (255.255.255.192)

# Converte os octetos para binário '00001010000101000000110000101101'
ipv4 = ''.join([format(int(x), '08b') for x in ip.split('.')])
num_bits_mascara = int(mascara_subrede.split('/')[1])  # Extrai o 26 da string
mascara = ('1' * num_bits_mascara).ljust(32, '0')  # '11111111111111111111111111000000'


def ipv4_para_str(ipv4: int):
    return f'{(ipv4 & 0b11111111_00000000_00000000_00000000) >> 24}' \
           f'.{(ipv4 & 0b00000000_11111111_00000000_00000000) >> 16}' \
           f'.{(ipv4 & 0b00000000_00000000_11111111_00000000) >> 8}' \
           f'.{(ipv4 & 0b00000000_00000000_00000000_11111111) >> 0}'


def obter_dados_rede(ipv4: str, mascara: str):
    """
    Obtém todos os dados de range de ip de uma rede.

    :param ipv4: Cada um dos octetos na forma binária.
    Ex.: '00001010000101000000110000101101'
    :param mascara: Cada um dos octetos na forma binária.
    Ex.: '11111111111111111111111111000000'

    :return: O ipv4, a máscara, o número de hosts, o ip da rede, o ip de broadcast,
    o primeiro ip e o último ip todos em números decimais.
    """

    num_zeros = mascara.count('0')
    num_hosts = 2 ** num_zeros - 2
    ipv4_num = int(ipv4, 2)        # 00001010000101000000110000101101 para decimal 169085997
    mascara_num = int(mascara, 2)  # 11111111111111111111111111000000 para 4294967232
    ipv4_rede_num = ipv4_num & mascara_num  # Zera os últimos bits do ipv4
    # Ao negar (~) 11111111111111111111111111000000 temos 00000000000000000000000000111111
    ipv4_broadcast_num = ipv4_num | ~mascara_num  # Ativa os últimos bits do ipv4
    ipv4_primeiro_num = ipv4_rede_num + 1
    ipv4_ultimo_num = ipv4_broadcast_num - 1

    return ipv4_para_str(ipv4_num), ipv4_para_str(mascara_num), num_hosts, \
           ipv4_para_str(ipv4_rede_num), ipv4_para_str(ipv4_broadcast_num), \
           ipv4_para_str(ipv4_primeiro_num), ipv4_para_str(ipv4_ultimo_num)


print(obter_dados_rede(ipv4, mascara))
