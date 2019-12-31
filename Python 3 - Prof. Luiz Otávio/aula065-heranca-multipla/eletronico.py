class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self.ligado = False

    def ligar(self):
        if (self.ligado):
            print(f'{self._nome} já está ligado')

        else:
            self.ligado = True
            print(f'{self._nome} foi ligado')

    def desligar(self):
        if (not self.ligado):
            print(f'{self._nome} já está desligado')

        else:
            self.ligado = False
            print(f'{self._nome} foi desligado')
