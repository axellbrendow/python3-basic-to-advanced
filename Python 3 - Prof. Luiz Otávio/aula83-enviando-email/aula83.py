from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart  # Assunto do email, quem envia e quem recebe
from email.mime.text import MIMEText  # Corpo do email ou texto em HTML
from email.mime.image import MIMEImage  # Anexar imagem ao email
import smtplib  # Conecta em um servidor e manda a mensagem

with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz Otávio', data=data)
    # Caso seja possível que alguma variável no template não seja passada para
    # a função .substitute, recomenda-se usar .safe_substitute() pois isso deixará
    # as variáveis do template intactas.

msg = MIMEMultipart()
msg['from'] = 'Axell'
msg['to'] = meu_email
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as imagem:
    img = MIMEImage(imagem.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Mensagem de hello
    smtp.starttls()  # O gmail aceita email com tls
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso!')
