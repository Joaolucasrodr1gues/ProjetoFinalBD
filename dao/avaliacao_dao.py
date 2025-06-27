from database.conexao import conectar
from models.avaliacao_model import Avaliacao

class AvaliacaoDAO:
    def inserir(self, nota, descricao, idpedido):
        con = conectar()
        cur = con.cursor()
        cur.execute('INSERT INTO avaliacao (nota, descricao, idpedido) VALUES (%s, %s, %s)',
                    (nota, descricao, idpedido))
        con.commit()
        cur.close()
        con.close()

    def listar_todas(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM avaliacao")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return [Avaliacao(*r) for r in resultado]

    @property
    def listar_com_cliente(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT avaliacao.idavaliacao, avaliacao.nota, avaliacao.descricao, cliente.nome
            FROM avaliacao
            JOIN pedido ON avaliacao.idpedido = pedido.idpedido
            JOIN cliente ON pedido.idcliente = cliente.idcliente
        """)
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado
