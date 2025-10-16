# Construa um programa que realiza o sorteio de um número entre 1 e 15
# O usuário terá 3 tentativas para acertar o número sorteado
# A cada tentativa, o programa deve informar se o número sorteado é maior ou menor do que o número digitado pelo usuário
# Caso o usuário acerte o número, o programa deve parabenizá-lo e encerrar
import random

def entradaUsuario():
    '''
    Função que realiza a entrada do usuário.

    Pede a entrada e tenta fazer a conversão para inteiro, usando um try-except para caso
    o usuário entre um valor não numérico.

    Função também realiza a validação do número entrado, caso esteja fora dos parâmetros
    esperados(entre 1 e 15).

    Função roda infinitamente e só para quando o usuário entra um valor válido.
    '''
    while True:
        try:
            entrada = int(input("Qual será o número?\n"))
        except ValueError as erro:
            print("Entrada inválida!")
            continue

        if 1 <= entrada <= 15:
            return entrada

        print("O valor deve estar entre 1 e 15")

def resultado(nSorte:int, nUsuario:int)->bool:
    '''
    Função para checar se o usuário acertou o valor ou não.

    nSorte:
        Parâmetro que recebe o valor sorteado

    nUsuario:
        Parâmetro que recebe o valor digitado pelo usuário
    '''
    if nUsuario < nSorte:
        print("Você chutou um valor baixo, tente novamente")
        return False
    elif nUsuario > nSorte:
        print("Você chutou um valor alto, tente novamente")
        return False
    else:
        print(f"Parabéns, você acertou o número!")
        print(f"O valor realmente era {nUsuario}.")
        return True

sorte = random.randint(1, 15)
print("Bem vindo a Loteria da Babilônia!\n" \
    "Um número entre 1 e 15 foi selecionado aleatoriamente.\n" \
    "Você possui 3 chances para acertar o número.\n" \
    "Boa sorte!")

for i in range(3):
    print(f"\nVocê está na tentativa número {i+1}")
    usuario = entradaUsuario()
    if resultado(nSorte=sorte, nUsuario=usuario):
        print(f"Você acerto na tentativa número {i+1}")
        break
