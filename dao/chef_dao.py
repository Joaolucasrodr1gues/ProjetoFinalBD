from database.conexao import conectar
from models.chef_model import Chef

class ChefDAO:
    def inserir(self, nome, especialidade, experiencia):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO chef (nome, especialidade, experiencia) VALUES (%s, %s, %s)",
                    (nome, especialidade, experiencia))
        con.commit()
        cur.close()
        con.close()

    def listar_todos(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM chef")
        resultado = cur.fetchall()
        cur.close()
        con.close()
        return [Chef(*c) for c in resultado]

    def buscar_por_id(self, idchef):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM chef WHERE idchef = %s", (idchef,))
        resultado = cur.fetchone()
        cur.close()
        con.close()
        return Chef(*resultado) if resultado else None
