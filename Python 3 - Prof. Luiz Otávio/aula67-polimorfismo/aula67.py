# abc = abstract base class
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
b.falar('assunto de B')

c = C()
c.falar('assunto de C')
