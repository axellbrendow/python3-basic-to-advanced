# Problema dos Angry Ducks. Deseja-se lançar um pato de uma certa altura
# com uma velocidade inicial e um ângulo e o pato deve cair no alvo.

import math

PI = 3.14159  # Constantes PI
G = 9.80665  # Gravidade


def resolver_equacao(a: float, b: float, c: float):
    """
    Resolve uma equação do 2º grau.

    :param a: Coeficiente do termo de 2º grau.
    :param b: Coeficiente do termo de 1º grau.
    :param c: Termo independente.

    :return: Caso o delta seja negativo, retorna dois valores iguais a math.inf.
        Caso contrário, retorna as duas raízes da equação.
    """
    x1 = math.inf
    x2 = math.inf
    delta = b * b - 4 * a * c

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2


altura_inicial = float(input())
x_inicio_alvo, x_fim_alvo = [int(x) for x in input().split()]
numero_de_tentativas = int(input())

for i in range(numero_de_tentativas):
    # Lê o ângulo e a velocidade inicial
    angulo_inicial, velocidade = [float(x) for x in input().split()]
    angulo_inicial = math.radians(angulo_inicial)

    # Calcula as velocidades iniciais
    velocidade_em_x = velocidade * math.cos(angulo_inicial)
    velocidade_inicial_em_y = velocidade * math.sin(angulo_inicial)

    # Já que a condição de parada é y = 0, é necessário encontrar uma equação
    # para y. Como o movimento na vertical (y) é uniformemente variado (MUV):
    # y = y_inicial + velocidade * tempo - (gravidade / 2) * tempo * tempo
    tempo1, tempo2 = resolver_equacao(-G / 2, velocidade_inicial_em_y, altura_inicial)
    # O tempo maior será o tempo de y = 0 após o vértice da parábola pois ela
    # tem concavidade para baixo
    tempo_na_queda = max(tempo1, tempo2)
    distancia_percorrida = velocidade_em_x * tempo_na_queda

    acertou = x_inicio_alvo <= distancia_percorrida <= x_fim_alvo
    print(f'{distancia_percorrida:.5f} -> {"DUCK" if acertou else "NUCK"}')
