import random
from datetime import datetime

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
now = datetime.now()
year = str(now.year).zfill(4)
month = str(now.month).zfill(2)
hour = str(now.hour).zfill(2)
minute = str(now.minute).zfill(2)
second = str(now.second).zfill(2)

for categoria_post_id in range(1, 5):  # Pressupõe 4 categorias
    for i in range(5):  # 5 posts para cada categoria
        titulo_post = ' '.join([''.join(random.choices(ALPHABET, k=random.randint(3, 8))) for i in range(3)])
        data_post = f'{year}-{month}-{str((now.day - i) % 29).zfill(2)} {hour}:{minute}:{second}'
        conteudo_post = (titulo_post + ' says:' + ' python' * random.randint(3, 25) + '.</br>') * 5
        excerto_post = titulo_post + ' says:' + ' python' * random.randint(3, 25) + '.'
        imagem_post = f'post_img/2020/01/27/MasterYi.jpg'  # Mude para uma imagem que você tenha feito upload
        publicado_post = random.randint(0, 1)
        autor_post_id = 1  # id do seu super usuário

        sql_post = (f"INSERT INTO blog_django.posts_post"
                          f"(titulo_post,data_post,conteudo_post,excerto_post,imagem_post,"
                          f"publicado_post,autor_post_id,categoria_post_id)"
                          f"VALUES ('{titulo_post}','{data_post}','{conteudo_post}',"
                          f"'{excerto_post}','{imagem_post}',{publicado_post},"
                          f"{autor_post_id},{categoria_post_id});")

        print(sql_post)
        print()
