"""
Abstração, Herança, Encapsulamento e Polimorfismo
Criar uma classe Cliente que herda da classe Pessoa (Herança)
    Cliente TEM conta (Agregação)
Criar classes ContaPoupanca e ContaCorrente que herdam da Conta
    Conta deve ter o método abstrato sacar(Abstração e polimorfismo)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se a autenticação do banco for verdadeira
"""

from banco.Agencia import Agencia
from banco.Cliente import Cliente
from banco.Banco import Banco
from banco.ContaCorrente import ContaCorrente
from banco.ContaPoupanca import ContaPoupanca

agencias = [
    Agencia(1, 'Santander'),
    Agencia(2, 'Santander'),
    Agencia(3, 'BB'),
    Agencia(4, 'BB'),
    Agencia(5, 'Itaú'),
    Agencia(6, 'Itaú'),
]

clientes = [
    Cliente('cliente1', 19, agencias[0]),
    Cliente('cliente2', 19, agencias[1]),
    Cliente('cliente3', 19, agencias[2]),
    Cliente('cliente4', 19, agencias[3]),
    Cliente('cliente5', 19, agencias[4]),
    Cliente('cliente6', 19, agencias[5]),
]

contas = [
    ContaCorrente(agencias[0], 1, clientes[0], 200, 500),
    ContaCorrente(agencias[1], 2, clientes[1], 200, 500),
    ContaCorrente(agencias[2], 3, clientes[2], 200, 500),
    ContaCorrente(agencias[3], 4, clientes[3], 200, 500),
    ContaCorrente(agencias[4], 5, clientes[4], 200, 500),
    ContaCorrente(agencias[5], 6, clientes[5], 200, 500),
    ContaPoupanca(agencias[0], 7, clientes[0], 200),
    ContaPoupanca(agencias[1], 8, clientes[1], 200),
    ContaPoupanca(agencias[2], 9, clientes[2], 200),
    ContaPoupanca(agencias[3], 10, clientes[3], 200),
    ContaPoupanca(agencias[4], 11, clientes[4], 200),
    ContaPoupanca(agencias[5], 12, clientes[5], 200),
]

bancos = [
    Banco('Santander', agencias, clientes, contas),
    Banco('BB', agencias, clientes, contas),
    Banco('Itaú', agencias, clientes, contas),
]

print('\nSacando em todos os bancos, usando todos os clientes e todas as contas\n')

for banco in bancos:
    for cliente in banco.clientes:
        print(banco)
        print(cliente)
        print()

        for conta in banco.contas:
            banco.sacar(cliente, conta, 100)

        print()
