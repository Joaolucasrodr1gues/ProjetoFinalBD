from database.conexao import conectar
from models.pedido_model import Pedido

class PedidoDAO:
    def inserir(self, precototal, pagamento, idcliente, idrestaurante):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO pedido (precototal, pagamento, idcliente, idrestaurante) VALUES (%s, %s, %s, %s)",
                    (precototal, pagamento, idcliente, idrestaurante))
        con.commit()
        cur.close()
        con.close()

    def listar_todos(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM pedido")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return [Pedido(*p) for p in resultado]

    def listar_completo(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT pedido.idpedido, cliente.nome, restaurante.nome, pedido.precototal
            FROM pedido
            JOIN cliente ON pedido.idcliente = cliente.idcliente
            JOIN restaurante ON pedido.idrestaurante = restaurante.idrestaurante
        """)
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado
