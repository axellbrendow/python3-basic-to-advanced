from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict) -> Union[str, float]:
    """
    Esta função retorna 10.10 caso o dicionário tenha apenas uma propriedade.
    Caso contrário, ela retorna o float + a string (descrição rápida)

    (descrição longa) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
    tincidunt magna a justo viverra, sit amet feugiat dui tempus. Nullam dictum lectus
    at urna vehicula pharetra. Cras arcu mi, vulputate ac est quis, vulputate porttitor
    mauris. Aliquam magna nulla, viverra et sem vel, consectetur condimentum magna.
    Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
    Vestibulum quis nisl nec odio porttitor suscipit sed id quam. In vel nibh non tellus
    sodales aliquam. Integer eget dapibus diam. Nullam hendrerit odio finibus velit
    malesuada sagittis. Nullam efficitur magna tellus, vel porta turpis finibus in. Ut ac
    diam ante.

    :param p1: float a ser somado com a string.
    :type p1: float
    :param p2: string a ser somada com o float.
    :type p2: str
    :param p3: dict aleatório.
    :type p3: dict

    :return: o float + a string
    :rtype: str

    :raises ValueError: Se o dicionário p3 não estiver vazio.
    """

    if p3:
        raise ValueError()

    if len(p3) == 1:
        return 10.10

    else:
        return str(p1) + p2


print(funcao(10.1, 'str', {}))
print(len({'nome': 'axell'}))
