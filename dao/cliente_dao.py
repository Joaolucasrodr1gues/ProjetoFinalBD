from database.conexao import conectar

class ClienteDAO:
    def inserir(self, nome, telefone, endereco, email, senha):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO cliente (nome, telefone, endereco, email, senha) VALUES (%s, %s, %s, %s, %s)",
                    (nome, telefone, endereco, email, senha))
        con.commit()
        cur.close()
        con.close()

    def atualizar(self, idcliente, campo, novo_valor):
        con = conectar()
        cur = con.cursor()
        cur.execute(f"UPDATE cliente SET {campo} = %s WHERE idcliente = %s", (novo_valor, idcliente))
        con.commit()
        cur.close()
        con.close()

    def deletar(self, idcliente):
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM cliente WHERE idcliente = %s", (idcliente,))
        con.commit()
        cur.close()
        con.close()

    def listar_todos(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM cliente")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado

    def buscar_por_id(self, idcliente):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM cliente WHERE idcliente = %s", (idcliente,))
        resultado = cur.fetchone()
        cur.close()
        con.close()
        return resultado

    def buscar_com_pedidos(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT cliente.nome, pedido.idpedido, pedido.precototal
            FROM cliente
            JOIN pedido ON cliente.idcliente = pedido.idcliente
        """)
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado
