#cada produto na venda terá: nome, preço e quantidade
lista = []

def incluir_item():
    print("### incluindo produto ###")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produto = {"nome":  nome, "preco": preco,
               "quantidade": quantidade}
    lista.append(produto)

def mostrar_venda():
    total_venda = 0
    for item in lista:
        total_item = (item['preco'] * item['quantidade'])
        print("=== Produto ===")
        print("Nome:", item['nome'], "Quantidade:",
                item['quantidade'], "Preço: ",
                item['preco'], "Total:",
                total_item
                )
        total_venda += total_item
    print("Total da venda: ", total_venda)

while (True):
    print("1-Incluir item\t 2-Mostrar Venda\t 3-Sair.")
    opcao = input("Digite a opção: ")
    
    if opcao == '1':
        incluir_item()
    elif opcao == '2':
        mostrar_venda()
    elif opcao == '3':
        break
    else:
        print("Opção inválida!")