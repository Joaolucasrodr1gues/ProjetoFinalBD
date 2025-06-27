from database.conexao import conectar
from models.produto_model import Produto

class ProdutoDAO:
    def inserir(self, tipo, quantidade):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO produto (tipo, quantidade) VALUES (%s, %s)", (tipo, quantidade))
        con.commit()
        cur.close()
        con.close()

    def listar_todos(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM produto")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return [Produto(*p) for p in resultado]

    def buscar_por_tipo(self, tipo):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM produto WHERE tipo = %s", (tipo,))
        resultado = cur.fetchone()
        cur.close()
        con.close()
        return Produto(*resultado) if resultado else None
