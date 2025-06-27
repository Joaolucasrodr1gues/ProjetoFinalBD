from database.conexao import conectar
from models.restaurante_model import Restaurante




def inserir_restaurante():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Nome do restaurante: ")
    endereco = input("Endereço: ")

    # Mostrar chefs disponíveis
    cursor.execute("SELECT idchef, nome FROM chef")
    chefs = cursor.fetchall()
    print("\n--- Chefs disponíveis ---")
    for idchef, nome_chef in chefs:
        print(f"ID: {idchef} | Nome: {nome_chef}")

    idchef = input("Informe o ID do chef responsável: ")

    sql = "INSERT INTO restaurante (nome, endereco, idchef) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, endereco, idchef))
    conn.commit()
    print("Restaurante inserido com sucesso.\n")
    conn.close()


def atualizar_endereco_restaurante():
    conn = conectar()
    cursor = conn.cursor()
    idrestaurante = input("ID do restaurante: ")
    novo_endereco = input("Novo endereço: ")
    sql = "UPDATE restaurante SET endereco = %s WHERE idrestaurante = %s"
    cursor.execute(sql, (novo_endereco, idrestaurante))
    conn.commit()
    print("Endereço atualizado com sucesso.\n")
    conn.close()


def deletar_restaurante():
    conn = conectar()
    cursor = conn.cursor()
    idrestaurante = input("ID do restaurante a ser deletado: ")
    sql = "DELETE FROM restaurante WHERE idrestaurante = %s"
    cursor.execute(sql, (idrestaurante,))
    conn.commit()
    print("Restaurante deletado com sucesso.\n")
    conn.close()


def listar_restaurantes():
    conn = conectar()
    cursor = conn.cursor()
    sql = """
          SELECT r.idrestaurante, r.nome, r.endereco, c.nome AS chef
          FROM restaurante r
                   JOIN chef c ON r.idchef = c.idchef \
          """
    cursor.execute(sql)
    for (idrestaurante, nome, endereco, chef) in cursor.fetchall():
        print(f"ID: {idrestaurante} | Nome: {nome} | Endereço: {endereco} | Chef: {chef}")
    conn.close()


def buscar_restaurante_por_id():
    conn = conectar()
    cursor = conn.cursor()
    idrestaurante = input("ID do restaurante: ")
    sql = """
          SELECT r.nome, r.endereco, c.nome AS chef
          FROM restaurante r
                   JOIN chef c ON r.idchef = c.idchef
          WHERE r.idrestaurante = %s \
          """
    cursor.execute(sql, (idrestaurante,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"Nome: {resultado[0]} | Endereço: {resultado[1]} | Chef: {resultado[2]}")
    else:
        print("Restaurante não encontrado.")
    conn.close()
