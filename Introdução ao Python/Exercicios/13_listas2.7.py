#%%
frutas = {"maçã":1.5, "pera":1.25, "goiaba":2.15, "banana":2.75
          , "laranja":0.65, "abacaxi":3.20, "uva":1.90, "limão":1.25
          , "jaca":5.8}

# %%
fruta = input("Digite o nome da fruta: ").lower()
if fruta in frutas:
    print(f"O preço dessa fruta é: R${frutas[fruta]}")
else:
    print("Essa fruta não está disponível")
# %%
