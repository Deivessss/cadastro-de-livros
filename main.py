#biblioteca responsável por conectar o Python ao MySQL
import mysql.connector
from mysql.connector import Error

#função para realizar a conexão com o MySQL:
def conexao_mysql():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cadastro_de_livros"
        )
        if conexao.is_connected():
            return conexao
    except Error as erro:
        print(f"Erro ao conectar no banco de dados: {erro}")

#função para cadastrar um novo livro:
def cadastrar_livro():
    conexao = None
    cursor = None
    try:
        conexao = conexao_mysql()
        if conexao.is_connected():
            print("-" * 46)
            print("-" * 12, "MENU CADASTRAR LIVRO", "-" * 12)
            nome = input("Informe o nome do livro: ").capitalize().strip()
            autor = input("Informe o autor do livro: ").capitalize().strip()
            editora = input("Informe a editora do livro: ").capitalize().strip()

            cursor = conexao.cursor()
            sql = "INSERT INTO livros (nome, autor, editora) VALUES (%s, %s, %s)"
            valores = (nome, autor, editora)
            cursor.execute(sql, valores)
            conexao.commit()

            print(f"Livro {nome} cadastrado com sucesso! ID: {cursor.lastrowid}")
    except Error as erro:
        print(f"Erro ao inserir o livro: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

#função para consultar os livros já cadastrados:
def consultar_livro():
    conexao = None
    cursor = None
    while True:
        try:
            print("-" * 46)
            print("-" * 12, "MENU CONSULTAR LIVRO", "-" * 12)
            opcao = int(input("Escolha a opção desejada:\n"
                              "1 - Consultar Todos os Livros\n"
                              "2 - Consultar Livro por id\n"
                              "3 - Consultar Livro(s) por autor\n"
                              "4 - Retornar para o Menu Principal\n"
                              ">>"))
        except ValueError:
            print("Erro. Digite apenas números (1,2,3 ou 4).")
            continue

        if opcao == 1:
            try:
                conexao = conexao_mysql()
                if conexao.is_connected():
                    cursor = conexao.cursor()
                    sql = "SELECT * FROM livros"
                    cursor.execute(sql)
                    resultado = cursor.fetchall()

                    for livro in resultado:
                        print("-" * 46)
                        print(f"ID: {livro[0]}\n"
                              f"Nome: {livro[1]}\n"
                              f"Autor: {livro[2]}\n"
                              f"Editora: {livro[3]}")
                        print("-" * 46)
            except Error as erro:
                print(f"Erro ao consultar os livros: {erro}")
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()

        elif opcao == 2:
            id_consulta = int(input("Informe o ID: "))
            try:
                conexao = conexao_mysql()
                if conexao.is_connected():
                    cursor = conexao.cursor()
                    sql = "SELECT * FROM livros WHERE id = %s"
                    valor = (id_consulta,) # vírgula no final cria uma tupla de um item
                    cursor.execute(sql, valor)
                    resultado = cursor.fetchone()
                    if resultado:
                        print("-" * 46)
                        print(f"ID: {resultado[0]}\n"
                              f"Nome: {resultado[1]}\n"
                              f"Autor: {resultado[2]}\n"
                              f"Editora: {resultado[3]}")
                        print("-" * 46)
                    else:
                        print("Nenhum livro encontrado com esse ID.")
            except Error as erro:
                print(f"Erro ao consultar o livro: {erro}")
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()

        elif opcao == 3:
            autor = input("Informe o autor: ").capitalize().strip()
            try:
                conexao = conexao_mysql()
                if conexao.is_connected():
                    cursor = conexao.cursor()
                    sql = "SELECT * FROM livros WHERE autor = %s"
                    valor = (autor,)
                    cursor.execute(sql, valor)
                    resultado = cursor.fetchall()
                    if resultado:
                        for livro in resultado:
                            print("-" * 46)
                            print(f"ID: {livro[0]}\n"
                                  f"Nome: {livro[1]}\n"
                                  f"Autor: {livro[2]}\n"
                                  f"Editora: {livro[3]}")
                            print("-" * 46)
                    else:
                        print("Nenhum livro encontrado com esse Autor.")
            except Error as erro:
                print(f"Erro ao consultar o livro: {erro}")
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()

        elif opcao == 4:
            break
        else:
            print("Opção inválida. Selecione apenas 1,2,3 ou 4.")

#função para remover um livro:
def remover_livro():
    conexao = None
    cursor = None
    try:
        conexao = conexao_mysql()
        if conexao.is_connected():
            remover = int(input("Digite o id do livro a ser removido: "))

            cursor = conexao.cursor()
            sql = "DELETE FROM livros WHERE id = %s"
            valor = (remover,)# vírgula no final cria uma tupla de um item
            cursor.execute(sql, valor)
            conexao.commit()

            if cursor.rowcount > 0:
                print(f"Livro de ID {remover} removido com sucesso.")
            else:
                print("Nenhum livro encontrado com esse ID")
    except Error as erro:
        print(f"Houve um erro: {erro}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


#código main onde o usuário vai escolher o que deseja:
print("Bem vindo a Livraria do Davi!")
while True:
    try:
        print("-" * 46)
        print("-" * 15, 'MENU PRINCIPAL', '-' * 15)
        escolha = int(input("Escolha a opção desejada:\n"
                            "1 - Cadastrar Livro\n"
                            "2 - Consultar Livro(s)\n"
                            "3 - Remover Livro\n"
                            "4 - Sair do Programa\n"
                            ">>"))
    except ValueError:
        print("Erro. Digite apenas números (1, 2, 3 ou 4).")
        continue

    if escolha == 1:
        cadastrar_livro()
    elif escolha == 2:
        consultar_livro()
    elif escolha == 3:
        remover_livro()
    elif escolha == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
        continue
