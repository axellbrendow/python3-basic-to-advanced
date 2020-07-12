import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='mysqlpass',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao

    finally:
        conexao.close()


# with conectar() as conexao:  # Já fecha a conexão
#     with conexao.cursor() as cursor:  # Já fecha o cursor
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()


# with conectar() as conexao:  # Já fecha a conexão
#     with conexao.cursor() as cursor:  # Já fecha o cursor
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('Muriel', 'Figueiredo', 19, 55),
#             ('Rose', 'Figueiredo', 19, 55),
#             ('José', 'Figueiredo', 19, 55),
#         ]
#
#         cursor.executemany(sql, dados)
#
#         conexao.commit()


# with conectar() as conexao:  # Já fecha a conexão
#     with conexao.cursor() as cursor:  # Já fecha o cursor
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#
#         conexao.commit()


with conectar() as conexao:  # Já fecha a conexão
    with conexao.cursor() as cursor:  # Já fecha o cursor
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Joana', 5))
        conexao.commit()


with conectar() as conexao:  # Já fecha a conexão
    with conexao.cursor() as cursor:  # Já fecha o cursor
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for dicionario in resultado:
            print(dicionario)
