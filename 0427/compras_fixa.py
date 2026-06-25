#Crie uma lista de compras com produtos
#Cada produto terá nome, preço, quantidade
#Mostre todos os produtos da lista e o valor total da compra

produtos = [
    {'nome': 'Banana', 'preco': 5.6, 'quantidade': 3},
    {'nome': 'Maçã', 'preco': 8.5, 'quantidade': 2},
    {'nome': 'Laranja', 'preco': 3.5, 'quantidade': 4}
]

valor_total = 0

for prod in produtos:
    print(f"Nome: {prod['nome']}", f"Preço: {prod['preco']}",
          f"Quantidade: {prod['quantidade']}")
    valor_total += (prod['preco'] * prod['quantidade'])

print("Valor total da compra:", valor_total)