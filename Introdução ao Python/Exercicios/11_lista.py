lista = [1,2,1,1,2,4,1,5,2,6,4,1,2,58,7,4,1,5,8,2,5,42,4,1,1]
numero = int(input("Entre com o número a ser contado\n"))
contador = 0
for i in lista:
    if i == numero:
        contador += 1
print(f"O número {numero} aparece {contador} vezes na lista")