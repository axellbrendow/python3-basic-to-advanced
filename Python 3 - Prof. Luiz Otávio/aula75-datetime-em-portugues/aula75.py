from datetime import datetime, timedelta
from locale import LC_ALL, setlocale
from calendar import mdays  # Isso é um arranjo com o último dia de todos os meses

setlocale(LC_ALL, '') # '' deveria ser 'pt_BR.utf-8'

data1 = datetime.now()
mes_atual = int(data1.strftime('%m'))

# %A = dia da semana por extenso, %B = mês por extenso
print(data1.strftime('%A, %d de %B de %Y'))
print(mdays[mes_atual])
