livros = []

def adicionar_livros():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano_publicacao = int(input("Ano de publicação: "))
    disponivel = input("Disponível Sim/Não: ")

    livro = {"titulo": titulo, "autor": autor,
                "ano_publicacao": ano_publicacao, "disponivel": disponivel}
    
    livros.append(livro)

def lista_livros():
    for livro in livros:
        print(livro)

while (True):
    opcao = input("(1)-Adicionar livros (2)-Listar livros (3)-Sair: ")
    if (opcao == '3'):
        break
    elif (opcao == '2'):
        lista_livros()
    elif (opcao == '1'):
        adicionar_livros()
    else:
        print("Opção inválida!")