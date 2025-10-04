print("Bem vindo a venda de água!")
print("Você pode comprar água mineral natural(1) ou com gás(2)")
print("Qual você escolhe?")
decisao = int(input())
if decisao == 1:
    print("Você escolheu água mineral natural")
    print("O total fica R$1,50")
    print("Obrigado por visitar nossa loja!")
elif decisao == 2:
    print("Você escolheu água mineral com gás")
    print("O total fica R$2,50")
    print("Obrigado por visitar nossa loja!")
else:
    print("Você não escolheu nenhuma das opções")
    print("Obrigado por visitar nossa loja!")