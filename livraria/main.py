def buscar_por_isbn_ou_titulo(livros, termo_busca):
    """Buscar um livro pelo ISBN ou pelo título e retorna o ISBN do livro encontrado"""
    if termo_busca.isdigit() and termo_busca in livros:
        return termo_busca # retorna o ISBN se livro encontrado #
    else:
        for isbn, livro in livros.items():
            if livro['Título'].lower() == termo_busca.lower():
                return isbn # retorna o ISBN se livro encontrado #
    return None # retorna none se livro não encontrado #
def livraria():
    livros = {}
    while True:
        print("\nMenu")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Atualizar Livro")
        print("4. Remover Livro")
        print("5. Lista de Livros")
        print("6. Relatorio de Livros")
        print("7. Fechar")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            isbn = input("Digite o ISBN do Livro: ")
            if isbn in livros:
                print("Livro já cadastrado!")
            else:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano_publicacao = input("Digite o ano de publicação do livro: ")
                quantidade = input("Digite a quantidade de estoque: ")
                livros[isbn] = {"Título": titulo, "Autor": autor, "Ano de publicação": ano_publicacao, "Quantidade de estoque": quantidade}
                print(f"Livro '{titulo}' cadastrado com sucesso!")

        elif opcao == "2":
            termo_busca = input("Digite o Isbn ou o Título do livro que deseja buscar: ")
            isbn_encontrado = buscar_por_isbn_ou_titulo(livros, termo_busca)
            if isbn_encontrado:
                livro = livros[isbn_encontrado]
                print(f"\nLivro encontrado - ISBN: {isbn_encontrado}")
                print(f"Título: {livro['Título']}")
                print(f"Autor: {livro['Autor']}")
                print(f"Ano de publicação: {livro['Ano de publicação']}")
                print(f"Quantidade em estoque: {livro['Quantidade de estoque']}")
            else:
                print("Livro não encontrado!")

        elif opcao == "3":
            termo_busca = input("Digite o ISBN ou o título do Livro que deseja atualizar: ")
            isbn_encontrado = buscar_por_isbn_ou_titulo(livros, termo_busca)
            if isbn_encontrado:
                print("Qual informação do livro deseja alterar?")
                print("1. Título")
                print("2. Autor")
                print("3. Ano de publicação")
                print("4. quantidade de estoque")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    novo_titulo = input("Digite o novo título: ")
                    livros[isbn_encontrado]['Título'] = novo_titulo
                elif escolha == "2":
                    novo_autor = input("Digite o nome do novo autor: ")
                    livros[isbn_encontrado]['Autor'] = novo_autor
                elif escolha == "3":
                    novo_ano = input("Digite o novo ano de publicação: ")
                    livros[isbn_encontrado]['Ano de publicação'] = novo_ano
                elif escolha == "4":
                    nova_quantidade = input("Digite a nova quantidade de estoque: ")
                    livros[isbn_encontrado]['Quantidade de estoque'] = nova_quantidade
                else:
                    print("Opção inválida, escolha uma opção válida.")
                print("Livro atualizado com sucesso!")

            else:
                print("Livro não encontrado!")

        elif opcao == "4":
            termo_busca = input("Digite o ISBN ou o título do livro que deseja remover: ")
            isbn_encontrado = buscar_por_isbn_ou_titulo(livros, termo_busca)
            if isbn_encontrado:
                del livros[isbn_encontrado]
                print(f"Livro com ISBN {isbn_encontrado} removido com sucesso")
            else:
                print("Livro não encontrado!")

        elif opcao == "5":
            if livros:
                print("\nLista de todos os livros cadastrados: ")
                for isbn, dados in livros.items():
                    print(f"ISBN: {isbn}, Título: {dados['Título']}, Autor: {dados['Autor']}, Ano de publicação: {dados['Ano de publicação']}, Quantidade de estoque: {dados['Quantidade de estoque']}")
            else:
                print("Nenhum livro encontrado.")

        elif opcao == "6":
            print("\nRelatório de Estoque: ")
            for isbn, dados in livros.items():
                print(f"ISBN: {isbn}, Título: {dados['Título']}, Quantidade de estoque: {dados['Quantidade de estoque']}")

        elif opcao == "7":
            print("Fechando o sistema... Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolher opção válida.")

livraria()