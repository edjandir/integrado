nota = float(input("Qual a sua nota? "))

if (nota > 10 or nota < 0):
    print("Nota inválida!")
elif (nota >= 9):
    print("Excelente")
elif (nota >= 7):
    print("Bom")
elif (nota >= 5):
    print("Regular")
else:
    print("Reprovado")