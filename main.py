#lista onde todos os livros ficarão armazenados em formato de dicionário:
lista_livro = []
#acumulador para gerar o id dos livros:
id_global = 0


#função para cadastrar um livro novo:
def cadastrar_livro(id):
    print('-' * 46)
    print('-' * 12, 'MENU CADASTRAR LIVRO', '-' * 12)
    print(f'Id do livro: {id_global}')
    nome = input('Entre com o nome do livro: ').capitalize().strip()
    autor = input('Entre com o autor do livro: ').capitalize().strip()
    editora = input('Entre com a editora do livro: ').capitalize().strip()
    dicionario = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(dicionario)
    print('-' * 46, '\n')

#função para consultar os livros já cadastrados:
def consultar_livro():
    while True:
        try:
            print('-' * 46)
            print('-' * 12, 'MENU CONSULTAR LIVRO', '-' * 12)
            opcao = int(input('Escolha a opção desejada:\n'
                              '1 - Consultar Todos os Livros\n'
                              '2 - Consultar Livro por id\n'
                              '3 - Consultar Livro(s) por autor\n'
                              '4 - Retornar para o Menu Principal\n'
                              '>>'))
        except ValueError:
            print('Erro. Digite apenas números (1,2,3 ou 4).')
            continue

        if opcao == 1:
            for livro in lista_livro:
                print('-' * 7)
                print(f'id: {livro['id']}\n'
                      f'Nome: {livro['nome']}\n'
                      f'Autor: {livro['autor']}\n'
                      f'Editora: {livro['editora']}')
                print('-' * 7)
        elif opcao == 2:
            id_consulta = int(input('Informe o id: '))
            for livro in lista_livro:
                if id_consulta == livro['id']:
                    print('-' * 7)
                    print(f'id: {livro['id']}\n'
                          f'Nome: {livro['nome']}\n'
                          f'Autor: {livro['autor']}\n'
                          f'Editora: {livro['editora']}')
                    print('-' * 7)
        elif opcao == 3:
            autor = input('Informe o autor: ').capitalize().strip()
            for livro in lista_livro:
                if livro['autor'] == autor:
                    print('-' * 7)
                    print(f'id: {livro['id']}\n'
                          f'Nome: {livro['nome']}\n'
                          f'Autor: {livro['autor']}\n'
                          f'Editora: {livro['editora']}')
                    print('-' * 7)
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Selecione apenas 1,2,3 ou 4.')

#função para remover um livro:
def remover_livro():
    while True:
        try:
            remover = int(input('Digite o id do livro a ser removido: '))
            for livro in lista_livro:
                if remover == livro['id']:
                    lista_livro.remove(livro)
                    print(f"Livro de id {livro['id']} removido com sucesso.")
                    return
            print(f'Não há nenhum livro com ID {remover}')
        except ValueError:
            print('Erro. Digite apenas números (ID do livro).')


#código main onde o usuário vai escolher o que deseja:
print('Bem vindo a Livraria do Davi!')
while True:
    try:
        print('-' * 46)
        print('-' * 15, 'MENU PRINCIPAL', '-' * 15)
        escolha = int(input('Escolha a opção desejada:\n'
                            '1 - Cadastrar Livro\n'
                            '2 - Consultar Livro(s)\n'
                            '3 - Remover Livro\n'
                            '4 - Sair do Programa\n'
                            '>>'))
    except ValueError:
        print('Erro. Digite apenas números (1, 2, 3 ou 4).')

    if escolha == 1:
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha == 2:
        consultar_livro()
    elif escolha == 3:
        remover_livro()
    elif escolha == 4:
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida.')
        continue
