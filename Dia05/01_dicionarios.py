#%%
#Dicionários são pares de chave:valor
dados = {'Nome': 'Felipe',
         'Sobrenome': 'Loschi',
         'Idade': 21,
         'Altura': 1.71}
print(dados)
# %%
#Acessando valores
#print(dados[0]) -> Não funciona, pois não há chave '0'
print(dados['Nome'])
#%%
#Chaves são únicas, se repetir uma chave, o valor será atualizado
#Meu valor pode ser qualquer coisa, até mesmo uma lista ou outro dicionário
dados = {'Nome': 'Felipe',
         'Sobrenome': 'Loschi',
         'Idade': 21,
         'Altura': 1.71,
         'Hobbies': ['Programar', 'Correr', 'Jogar'],
         'Endereço': {'Rua': 'Rua A',
                      'Número': 123,
                      'Bairro': 'Centro'}}
print(dados['Hobbies'][-2])
# %%
#Podemos adicionar novos pares chave:valor
dados['Peso'] = 70
print(dados)
# %%
#Podemos pegar apenas as chaves ou apenas os valores
chaves = dados.keys()
valores = dados.values()
print(chaves)
print(valores)
# %%
#Podemos printar os pares chave:valor
itens = dados.items()
print(itens)
# %%
#Podemos iterar sobre os itens
for i in dados:
    print(i, " -> ", dados[i])    

# ou

for chave, valor in dados.items():
    print(f"A chave é {chave} e o valor é {valor}")

# %%
