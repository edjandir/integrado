meus_contatos=[
    {"nome": "Laura", "celular": "555555", "email": "laura@email.com"},
    {"nome": "João Vitor", "celular": "6666666", "email": "jvitor@email"},
    {"nome": "Lorenzo", "celular": "777777", "email": "lorenzo@email"}
]

#print(meus_contatos[2]["nome"],meus_contatos[2]["email"],)
for contato in meus_contatos:
    print(contato['nome'], contato['celular'], contato['email'])