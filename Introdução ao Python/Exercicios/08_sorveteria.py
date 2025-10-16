total = 0
escolha1 = 0
escolha2 = 0
print("Seja bem vindo a sorveteria Na Parede!")
print("Vamos montar seu sorvete?")
print("Primeiro escolha o seu tipo de sorvete:" \
"casquinha(1), cascão(2), cestinha(3)")
escolha1 = int(input())
if escolha1 == 1:
    print("Você escolheu casquinha(R$1,00)")
    total += 1
elif escolha1 == 2:
    print("Você escolheu cascão(R$2,50)")
    total += 2.5
elif escolha1 ==3:
    print("Você escolheu cestinha(R$4.00)")
    total += 4
else:
    print("Uai, não quer nada?")

print("Agora escolha o seu sabor de sorvete:" \
"morango(1), creme(2), chocolate(3)")
escolha2 = int(input())
if (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==1:
    print("Você escolheu sabor morango")
elif (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==2:
    print("Você escolheu sabor creme")
elif (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==3:
    print("Você escolheu sabor chocolate")
else:
    print("Uai, tá querendo um sabor que não existe ou tá querendo colocar sorvete no chão?")

print("Por último, escolha sobre cobertura:" \
"caramelo(1), chocolate(2), sem cobertura(3)")
escolha2 = int(input())
if (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==1:
    print("Você escolheu caramelo(R$1,50)")
    total += 2.5
elif (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==2:
    print("Você escolheu chocolate(R$1,50)")
    total += 1.5
elif (escolha1 == 1 or escolha1 == 2 or escolha1 == 3) and escolha2==3:
    print("Você escolheu sem cobertura")
else:
    print("Uai, tá querendo algo que não existe ou querendo colocar no chão?")

print(f"O seu total fica em R${total}")