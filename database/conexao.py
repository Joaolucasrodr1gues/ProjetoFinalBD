import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jl#24092001",  # troque pela sua senha
        database="mydb"
    )