from estoque import adicionar_produto, listar_estoque, valor_total_estoque, atualizar_estoque

lista = []

while(True):
    print("(1)Adicionar produto\n(2)Listar estoque" +
          "\n(3)Mostrar valor total estoque\n(4)Alterar quantidade do estoque\n(5)Sair")
    opcao = input("Digite a opção desejada: ")
    
    if (opcao == '1'):
        adicionar_produto(lista)
    elif (opcao == '2'):
        listar_estoque(lista)
    elif (opcao == '3'):
        print("Valor total do estoque: ", valor_total_estoque(lista))
    elif (opcao == '4'):
        atualizar_estoque(lista)
    elif (opcao == '5'):
        break
    else:
        print("Opção inválida!")
    
    print("Finalizado")