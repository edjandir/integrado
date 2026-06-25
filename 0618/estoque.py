import uuid

def adicionar_produto(lista):
    id = uuid.uuid4()
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite o estoque inicial do produto: "))
    produto = {'id': id, 'nome': nome, 'preco': preco, 'estoque': estoque}
    lista.append(produto)

def listar_estoque(lista):
    print("Estoque de produtos\nSeq - ID - Nome - Preço - Estoque")
    for indice, produto in enumerate(lista):
        print(f"{indice} - {produto['id']} - {produto['nome']} - {produto['preco']} - {produto['estoque']}")

def valor_total_estoque(lista):
    total = 0
    for produto in lista:
        total += (produto['preco'] * produto['estoque'])
    return total

def atualizar_estoque(lista):
    listar_estoque(lista)
    indice = int(input("Digite o indice do produto a ser alterado: "))
    nova_quantidade = int(input("Digite a nova quantidade: "))
    lista[indice]['estoque'] = nova_quantidade