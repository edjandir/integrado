def incluir_item(lista):
    print("### incluindo produto ###")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produto = {"nome":  nome, "preco": preco,
               "quantidade": quantidade}
    lista.append(produto)

def mostrar_venda(lista):
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

