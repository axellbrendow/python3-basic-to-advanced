from datetime import datetime
from random import randint

class Pessoa:
    # Isto é um atributo da classe, e não do objeto !
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def emitir(self, mensagem):
        print(f'{self.nome} {mensagem}.')

    def ano_de_nascimento(self):
        return self.ano_atual - self.idade

    def falar(self, assunto):
        if self.comendo:
            self.emitir('não pode falar pois está comendo')

        elif self.falando:
            self.emitir(f'já está falando')

        else:
            self.falando = True
            self.emitir(f'está falando sobre {assunto}')

    def parar_de_falar(self):
        if not self.falando:
            self.emitir(f'não está falando')

        else:
            self.falando = False
            self.emitir(f'parou de falar')

    def comer(self, alimento):
        if self.falando:
            self.emitir('não pode comer pois está falando')

        elif self.comendo:
            self.emitir(f'já está comendo')

        else:
            self.comendo = True
            self.emitir(f'está comendo {alimento}')

    def parar_de_comer(self):
        if not self.comendo:
            self.emitir(f'não está comendo')

        else:
            self.comendo = False
            self.emitir(f'parou de comer')

    @classmethod  # A classe é recebida como primeiro parâmetro
    def criar_por_ano_de_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        # Instancia um objeto da própria classe
        return cls(nome, idade)  # Factory method

    # Não tabalha com self nem cls. É apenas um método que fica no escopo da
    # classe e está sempre acessível.
    @staticmethod
    def gerarId():
        rand = randint(10000, 19999)
        return rand
