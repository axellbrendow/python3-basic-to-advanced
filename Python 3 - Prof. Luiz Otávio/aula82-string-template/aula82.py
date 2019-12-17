from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz Otávio', data=data)
    # Caso seja possível que alguma variável no template não seja passada para
    # a função .substitute, recomenda-se usar .safe_substitute() pois isso deixará
    # as variáveis do template intactas.

print(corpo_msg)
