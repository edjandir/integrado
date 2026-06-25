#Declare uma variável do tipo lista para guardar notas.
# Peça para o usuário digitar as notas. Só para quando
# o usuário digitar -1 (ou um valor negativo)
# ao final calcule o a média das notas.
# apresentar a maior nota e a menor nota.
notas = []
soma = 0

while(True):
    nota = int(input("Digite a nota: "))
    if (nota < 0):
        break
    elif (nota > 10):
        continue
    else:
        notas.append(nota)

if (len(notas)==0):
    print("Não há notas na avaliação.")
else:
    menor= notas[0]
    maior= notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
        if nota > maior:
            maior = nota
        soma+= nota
    print("A média das notas é:", (soma/len(notas)))
    print("A menor nota é", menor)
    print("A maior nota é", maior)