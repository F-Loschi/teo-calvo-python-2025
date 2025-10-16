#%%
nome = 'Felipe Silva Loschi'

for letra in nome:
    print(letra)
# %%
min_numero = int(input("Entre o ínicio da tabuada: "))
max_numero = int(input("Entre a parada da tabuada: "))
numero = int(input("Entre o número da tabuada: "))

for i in range(min_numero, max_numero+1):
    print(f"{numero} x {i} = {numero*i}")
# %%
for i in range(4,101):
    if i % 4 == 0:
        print(i)
# %%
