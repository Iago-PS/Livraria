import os

mensagens = []

nome = input("nome:")

while True:
    os.system('cls')

    if len (mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("________________")

    texto = input("mensagem:")
    if texto == "fim":
        break

    mensagens.append({
        "nome" : nome,
        "texto": texto
    })