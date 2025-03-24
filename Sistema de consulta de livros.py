print('Bem vindo a biblioteca de Leonardo Argenta')  # Mensagem de boas vindas
lista_livro = []  # Criação da lista de livros vazia
id_global = 0  # Criação do id global


def cadastrar_livros(id):
    # Input do nome do livro
    nome = input('Digite o nome do livro que quer cadastrar \n')
    # Input do nome do autor
    autor = input('Digite o nome do autor do livro \n')
    # Input do nome da editora
    editora = input('Digite o nome da editora do livro \n')

    livro = {"id": id, "nome": nome, "autor": autor,
             "editora": editora}  # Criação do dicionário do livro
    lista_livro.append(livro)  # Adição do livro na lista de livros
    print("Livro cadastrado com sucesso!\n")


def consultar_livro():  # Função para consultar o livro
    while True:
        print('Como deseja consultar o livro?z\n')
        print('1 - Consultar por Todos\n')
        print('2 - Consultar por Id\n')
        print('3 - Consultar por Autor\n')
        print('4 - Retornar ao Menu\n')
        opcao = input('Digite a opção desejada\n')
        if opcao == '1':  # Consultar todos os livros
            if len(lista_livro) == 0:
                print('Nenhum livro cadastrado\n')
            else:
                for livro in lista_livro:
                    print(livro)
        elif opcao == '2':  # Consultar por id
            id = int(input('Digite o id do livro que deseja consultar\n'))
            for livro in lista_livro:
                if livro['id'] == id:
                    print(livro)
                else:
                    print('Livro não encontrado\n')
        elif opcao == '3':  # Consultar por autor
            autor = input('Digite o autor que deseja consultar\n')
            for livro in lista_livro:
                if livro['autor'] == autor:
                    print(livro)
                else:
                    print('Autor não encontrado\n')
        elif opcao == '4':  # Retornar ao menu
            break
        else:
            print('Opção inválida, tente novamente\n')


def remover_livro():  # Função para remover o livro
    id = int(input('Digite o id do livro que deseja remover\n'))
    for livro in lista_livro:
        if livro['id'] == id:  # Verifica se o id é válido
            lista_livro.remove(livro)
            print('Livro removido com sucesso\n')
        else:  # Caso o id seja inválido
            print('Id Inválido\n')


while True:  # Loop do menu principal
    print('\nMenu Principal\n')
    print('1 - Cadastrar Livro\n')
    print('2 - Consultar Livro\n')
    print('3 - Remover Livro\n')
    print('4 - Encerrar programa\n')
    opcao = input('Digite a opção desejada\n')
    if opcao == '1':  # Cadastrar
        id_global += 1
        cadastrar_livros(id_global)
    elif opcao == '2':  # Consultar
        consultar_livro()
    elif opcao == '3':  # Remover
        remover_livro()
    elif opcao == '4':  # Encerrar
        break
    else:
        print('Opção inválida, tente novamente\n')
