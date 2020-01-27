import random

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for comentario_id in range(1, 6):  # 5 comentários por post
    for post_comentario_id in range(1, 21):  # Assume 20 posts criados
        nome_comentario = ''.join(random.choices(ALPHABET, k=8))
        email_comentario = f'{nome_comentario}@gmail.com'
        comentario = nome_comentario + ' says:' + ' python' * random.randint(3, 25) + '.'
        data_comentario = '2020-01-27 00:25:00'
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
