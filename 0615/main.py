from vendas import incluir_item, mostrar_venda

#cada produto na venda terá: nome, preço e quantidade
lista = []

while (True):
    print("1-Incluir item\t 2-Mostrar Venda\t 3-Sair.")
    opcao = input("Digite a opção: ")
    
    if opcao == '1':
        incluir_item(lista)
    elif opcao == '2':
        mostrar_venda(lista)
    elif opcao == '3':
        break
    else:
        print("Opção inválida!")