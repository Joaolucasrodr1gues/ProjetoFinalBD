from database.conexao import conectar
from models.receita_model import Receita

class ReceitaDAO:
    def inserir(self, dificuldade, nacionalidade, idchef):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO receita (dificuldade, nacionalidade, idchef) VALUES (%s, %s, %s)",
                    (dificuldade, nacionalidade, idchef))
        con.commit()
        cur.close()
        con.close()

    def listar_todas(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM receita")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return [Receita(*r) for r in resultado]

    def buscar_com_chef(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT receita.idreceita, receita.dificuldade, receita.nacionalidade, chef.nome
            FROM receita
            JOIN chef ON receita.idchef = chef.idchef
        """)
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return resultado
