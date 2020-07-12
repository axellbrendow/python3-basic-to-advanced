import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# Usar (?, ?) previne SQL Inject
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Luiz Otávio", 65.5))

# Usar (?, ?) previne SQL Inject
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {
#     "nome": "Maria",
#     "peso": 50.3
# })

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=2', {
#     'nome': 'Joana'
# })

# cursor.execute('DELETE FROM clientes WHERE id=:id', {
#     'id': 2
# })

conexao.commit()

cursor.execute('SELECT * FROM clientes WHERE peso > :peso', {
    'peso': 55
})

for cliente in cursor.fetchall():
    print(cliente)

cursor.close()
conexao.close()
