import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jl#24092001",
        database="mydb"
    )

def inserir_cliente():
    conn = conectar()
    cursor = conn.cursor()

    # Coleta dados do cliente
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    senha = input("Senha: ")

    # Insere cliente
    sql_cliente = "INSERT INTO cliente (nome, telefone, endereco, email, senha) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_cliente, (nome, telefone, endereco, email, senha))
    idcliente = cursor.lastrowid

    # Exibe os restaurantes disponíveis
    print("\n--- Restaurantes disponíveis ---")
    cursor.execute("SELECT idrestaurante, nome FROM restaurante")
    restaurantes = cursor.fetchall()

    if not restaurantes:
        print("Nenhum restaurante cadastrado. Insira um restaurante primeiro.")
        conn.rollback()
        conn.close()
        return

    for (idrest, nome) in restaurantes:
        print(f"ID: {idrest} | Nome: {nome}")

    # Coleta dados do pedido
    print("\n--- Cadastro de Pedido para o cliente ---")
    idrestaurante = input("Digite o ID do restaurante acima: ")
    preco = float(input("Preço total: "))
    pagamento = input("Forma de pagamento: ")

    sql_pedido = "INSERT INTO pedido (precototal, pagamento, idcliente, idrestaurante) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_pedido, (preco, pagamento, idcliente, idrestaurante))

    conn.commit()
    print("Cliente e pedido inseridos com sucesso.")
    conn.close()


def atualizar_email_cliente():
    conn = conectar()
    cursor = conn.cursor()
    idcliente = input("ID do cliente: ")
    novo_email = input("Novo email: ")
    sql = "UPDATE cliente SET email = %s WHERE idcliente = %s"
    cursor.execute(sql, (novo_email, idcliente))
    conn.commit()
    print("Email atualizado.")
    conn.close()

def deletar_cliente():
    conn = conectar()
    cursor = conn.cursor()
    idcliente = input("ID do cliente a deletar: ")
    sql = "DELETE FROM cliente WHERE idcliente = %s"
    cursor.execute(sql, (idcliente,))
    conn.commit()
    print("Cliente deletado.")
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    for (idcliente, nome, telefone, endereco, email, senha) in cursor.fetchall():
        print(f"ID: {idcliente} | Nome: {nome} | Email: {email}")
    conn.close()

def buscar_cliente_por_id():
    conn = conectar()
    cursor = conn.cursor()
    idcliente = input("ID do cliente: ")
    cursor.execute("SELECT * FROM cliente WHERE idcliente = %s", (idcliente,))
    cliente = cursor.fetchone()
    if cliente:
        print(f"Nome: {cliente[1]} | Email: {cliente[4]}")
    else:
        print("Cliente não encontrado.")
    conn.close()

def join_pedidos_cliente():
    conn = conectar()
    cursor = conn.cursor()
    sql = '''
    SELECT cliente.nome, cliente.email, pedido.idpedido, pedido.precototal
    FROM cliente
    JOIN pedido ON cliente.idcliente = pedido.idcliente
    '''
    cursor.execute(sql)
    for (nome, email, idpedido, total) in cursor.fetchall():
        print(f"Cliente: {nome} | Email: {email} | Pedido: {idpedido} | Total: R${total}")
    conn.close()


def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Inserir cliente")
        print("2. Atualizar email do cliente")
        print("3. Deletar cliente")
        print("4. Listar clientes")
        print("5. Buscar cliente por ID")
        print("6. Ver pedidos com nome e email do cliente")
        print("0. Sair")
        op = input("Escolha: ")
        if op == "1":
            inserir_cliente()
        elif op == "2":
            atualizar_email_cliente()
        elif op == "3":
            deletar_cliente()
        elif op == "4":
            listar_clientes()
        elif op == "5":
            buscar_cliente_por_id()
        elif op == "6":
            join_pedidos_cliente()
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
