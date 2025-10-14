#%%
idades = [17, 32, 56, 14, 28, 19, 42, 73, 15, 38]
print(idades)
#%%
idades.append(18)
print(idades)
#%%
idades_2 = []

while True:
    idade = int(input("Entre com a idade ou -1 para sair\n"))
    if idade == -1:
        break
    idades_2.append(idade)

media = sum(idades_2) / len(idades_2)
minimo = min(idades_2)
maximo = max(idades_2)
qtd = len(idades_2)

print(f"Média = {media}")
print(f"Mínimo = {minimo}")
print(f"Máximo = {maximo}")
print(f"Quantidade = {qtd}")
# %%
