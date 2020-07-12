"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False - 10 == 10
"""

print('Luiz'   , type('Luiz')                    )
print(10       , type(10)                        )
print(25.23    , type(25.23)                     )
print(10 == 10 , type(10 == 10)                  )
print('10'     , type('10')    , type(int('10')) )  # Converte str '10' para int 10

# Dados
# Nome: String
print('Axell', type('Axell'))

# Idade: int
print(19, type(19))

# Altura: float
print(1.8, type(1.8))

# Maior de idade: bool
print(19 > 18, type(19 > 18))
