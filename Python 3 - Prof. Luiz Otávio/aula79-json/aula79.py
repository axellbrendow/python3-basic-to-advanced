"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from dados import *
import json

# Converte um dicionário em JSON (dumps = dump string)
# útil para salvar informações de qualquer tipo
dados = json.dumps(clientes_dicionario, indent=4)

# Converte JSON em um dicionário (loads = load string)
# útil para carregar informações de qualquer tipo
dados = json.loads(clientes_json)
print(dados)

# Exporta dicionário para arquivo JSON (dump é em arquivo)
with open('clientes.json', 'w') as f:
    json.dump(clientes_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário (load é em arquivo)
with open('clientes.json', 'r') as f:
    data = json.load(f)

print(data)
