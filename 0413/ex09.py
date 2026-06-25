saldo = 0
opcao = 1

while(opcao !=3 ):
    if (opcao == 1):
        print(f"\nSeu saldo é: {saldo}")
    elif (opcao == 2):
        valor_deposito = float(input("Valor depósito: "))
        saldo += valor_deposito
    elif (opcao == 3):
        print("\nFinalizando...")
    else:
        print("\nOpção inválida!")
    opcao = int(input("\n(1)-saldo\t(2)-Despósito\t(3)-Sair:"))
print("\nFinalizando...")