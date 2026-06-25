pares=0
impares=0

for i in range(1,6):
    numero = int(input("Digite um número: "))

    if (numero % 2 == 0):
        pares+=1 # mesmo que pares++
    else:
        impares+=1 #mesmo que impares++

print(f"Pares: {pares}\nÍmpares: {impares}")