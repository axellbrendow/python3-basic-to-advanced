import random
from datetime import datetime

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
now = datetime.now()
year = str(now.year).zfill(4)
month = str(now.month).zfill(2)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)
second = str(now.second).zfill(2)

for i in range(1, 6):  # 5 comentários por post
    for post_comentario_id in range(1, 21):  # Assume 20 posts criados
        nome_comentario = ''.join(random.choices(ALPHABET, k=8))
        email_comentario = f'{nome_comentario}@gmail.com'
        comentario = nome_comentario + ' says:' + ' python' * random.randint(3, 25) + '.'
        data_comentario = f'{year}-{month}-{str((now.day - i) % 29).zfill(2)} {hour}:{minute}:{second}'
        publicado_comentario = random.randint(0, 1)
        usuario_comentario_id = 1  # id do seu super usuário

        sql_comentario = (f"INSERT INTO blog_django.comentarios_comentario"
                          f"(nome_comentario,email_comentario,comentario,data_comentario,"
                          f"publicado_comentario,post_comentario_id,usuario_comentario_id)"
                          f"VALUES ('{nome_comentario}','{email_comentario}','{comentario}',"
                          f"'{data_comentario}',{publicado_comentario},{post_comentario_id},"
                          f"{usuario_comentario_id});")

        print(sql_comentario)
        print()
