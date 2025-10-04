print(f"2 x 0 = 0")

#Vai rodar infinitamente
#while True:
#    print("Entrei no laço!")
#Por isso usamos um contador
contador = 0
while contador <= 10:
    print(f"Entrei no laço pela {contador + 1}ª vez")
    #Soma-se 1 a cada vez que entrar no laço para não entrar infinitamente
    contador += 1

#Podemos fazer a tabuada de um número qualquer
numero = int(input("Digite um número para ver sua tabuada: "))
contador = 0
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1