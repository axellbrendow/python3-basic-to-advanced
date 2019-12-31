class Agencia:
    def __init__(self, numero: int, banco: str):
        self.__numero = numero
        self.__banco = banco

    @property
    def numero(self):
        return self.__numero

    @property
    def banco(self):
        return self.__banco

    def __str__(self):
        return f"{{'numero': {self.__numero}, 'banco': {self.__banco}}}"

    def __eq__(self, other):
        return str(self) == str(other)
