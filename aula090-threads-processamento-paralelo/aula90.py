from time import sleep
from threading import Thread
from threading import Lock

"""
class MinhaThread(Thread):  # Forma de criar threads por classe
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self) -> None:
        sleep(self.tempo)
        print(self.texto)


t1 = MinhaThread('Thread 1', 5)
t1.start()

t2 = MinhaThread('Thread 2', 2)
t2.start()

t3 = MinhaThread('Thread 3', 3)
t3.start()
"""

"""
def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=(5, 'Olá mundo 1!'))
t1.start()

t2 = Thread(target=vai_demorar, args=(2, 'Olá mundo 2!'))
t2.start()

t3 = Thread(target=vai_demorar, args=(4, 'Olá mundo 3!'))
t3.start()

for i in range(10):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=(5, 'Olá mundo 1!'))
t1.start()

while t1.is_alive():
    print('Esperando a thread')
    sleep(1)

print('Thread acabou!')
"""

"""
t1 = Thread(target=vai_demorar, args=(5, 'Olá mundo 1!'))
t1.start()
t1.join()

print('Thread acabou!')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()  # Só uma thread pode passar dessa linha por vez

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')

        else:
            sleep(1)
            self.estoque -= quantidade

            print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque')

        self.lock.release()  # Não esquece de dar o release sempre


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(20):
        t = Thread(target=ingressos.comprar, args=(1,))
        t.start()
