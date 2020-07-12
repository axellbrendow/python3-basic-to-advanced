import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.connection = sqlite3.connect(arquivo)
        self.cursor = self.connection.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.connection.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.connection.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.connection.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)

        for tupla in self.cursor.fetchall():
            print(tupla)

    def buscar(self, nome):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{nome}%',))

        for tupla in self.cursor.fetchall():
            print(tupla)

    def fechar(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    agenda = AgendaDB('agendadb.db')
    agenda.inserir('Luiz', '11111111')
    agenda.inserir('Maria', '22222222')
    agenda.inserir('João', '33333333')
    agenda.inserir('Rose', '44444444')
    agenda.inserir('Guilherme', '55555555')
    agenda.inserir('Fabrício', '66666666')
    agenda.listar()
    print()
    agenda.editar('Francisco', '00000000', 1)
    agenda.listar()
    print()
    agenda.excluir(4)
    agenda.listar()
    print()
    agenda.buscar('e')
    print()
    agenda.fechar()
