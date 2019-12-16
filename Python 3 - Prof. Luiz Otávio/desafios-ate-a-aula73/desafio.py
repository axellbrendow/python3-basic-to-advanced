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


