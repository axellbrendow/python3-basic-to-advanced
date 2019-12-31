from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina)

maquina.escrever()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
