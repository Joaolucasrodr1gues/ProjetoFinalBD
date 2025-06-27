from database.conexao import conectar
from models.receita_has_produto_model import ReceitaProduto

class ReceitaProdutoDAO:
    def inserir(self, idreceita, idproduto):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO receita_has_produto (idreceita, idproduto) VALUES (%s, %s)",
                    (idreceita, idproduto))
        con.commit()
        cur.close()
        con.close()

    def deletar(self, idreceita, idproduto):
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM receita_has_produto WHERE idreceita = %s AND idproduto = %s",
                    (idreceita, idproduto))
        con.commit()
        cur.close()
        con.close()

    def listar_completo(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT r.idreceita, r.dificuldade, p.tipo
            FROM receita_has_produto rp
            JOIN receita r ON rp.idreceita = r.idreceita
            JOIN produto p ON rp.idproduto = p.idproduto
        """)
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado
