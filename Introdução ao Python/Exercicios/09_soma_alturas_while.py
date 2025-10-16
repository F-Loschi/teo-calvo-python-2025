soma = 0    #Valor final

qtde_entradas = 4   #Contador de entradas
while qtde_entradas > 0:
    altura = float(input("Entre com a altura\n"))
    soma += altura
    qtde_entradas -= 1

print(f"Soma das alturas = {soma}m")