#lista de compromissos
lista = []

#Adicionar os compromissos
while(True):
    print("\n--- Menu ---")
    print("1 - Adicionar compromisso")
    print("2 - Listar compromissos")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        data = input("Digite a data (dd/mm/aaaa): ")
        hora = input("Digite a hora (hh:mm): ")
        descricao = input("Digite a descrição: ")
        local = input("Diget o local: ")

        #cria um dicionário com os valores que o usuário digitou
        compromisso = {
            "data": data,
            "hora": hora,
            "descricao": descricao,
            "local": local
        }

        lista.append(compromisso)
        print("Compromisso adicionado com sucesso!")

    elif opcao == 2:
        if len(lista) == 0:
            print("Nenhum compromisso registrado.")
        else:
            for item in lista:
                print(item['data'], item['hora'], 
                      item['descricao'], item['local'])
                
    elif opcao == 3:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
        
