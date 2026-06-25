palavra = input("Digite uma palavra: ")
vogal = 0

for i in palavra:
    if i.lower() in "aáâãeéêiíoôóõuú":
        vogal+=1

print(f"A palavra tem {vogal} vogais.")