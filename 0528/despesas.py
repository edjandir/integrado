from datetime import datetime

lista = []

def texto_para_data(texto_data):
    return datetime.strptime(texto_data, "%d/%m/%Y")

def data_para_texto(data):
    return data.strftime("%d/%m/%Y")

def registrar_despesa():
    data = texto_para_data(input("Informe a data: "))
    valor = float(input("Informe o valor: "))
    categoria = input("Informe a categoria: ")
    descricao = input("Informe a descrição: ")

    despesa = {"data": data, "valor": valor,
                "categoria": categoria, "descricao": descricao}
    lista.append(despesa)

def mostrar_despesa(despesa):
    print("Data:", data_para_texto(despesa['data']), "Valor:", despesa['valor'],
            "Categoria", despesa['categoria'], "Descrição: ", despesa['descricao'])

def listar_despesas():
    for despesa in lista:
        mostrar_despesa(despesa)

def filtrar_categoria():
    categoria = input("Informe a categoria: ")
    for despesa in lista:
        if despesa['categoria'] == categoria:
            mostrar_despesa(despesa)

def filtrar_periodo():
    data1 = texto_para_data(input("Início do período: "))
    data2 = texto_para_data(input("Fim do período: "))
    for despesa in lista:
        if (despesa['data'] > data1) and (despesa['data'] < data2):
            mostrar_despesa(despesa)


while (True):
    opcao = input("1-Registrar\n2-Listar\n3-Filtrar por categoria\n4-Filtrar por período\n5-Sair\nOpção: ")

    if opcao == '1':
        registrar_despesa()
    elif opcao == '2':
        listar_despesas()
    elif opcao == '3':
        filtrar_categoria()
    elif opcao == '4':
        filtrar_periodo()
    elif opcao == '5':
        break
    else:
        print("Opção inválida!")
