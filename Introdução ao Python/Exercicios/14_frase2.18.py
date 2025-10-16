dados = {}

while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for dado in dados:
    print(f"A frase '{dado}' apareceu {dados[dado]} vezes")