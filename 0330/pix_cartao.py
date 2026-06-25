forma_pagto = input("Forma pago (P-Pix CC-Cartão de crédito): ")
valor_produto = float(input("Qual o valor do prouduto? "))


if (forma_pagto.upper() == 'P'):
    print(f"Pix. Desconto de 15%: {(valor_produto* 0.85)}")
elif (forma_pagto.upper() == 'CC'):
    print(f"Cartão. Valor normal: {valor_produto}")
else:
    print("Forma de pagamento inválida.")