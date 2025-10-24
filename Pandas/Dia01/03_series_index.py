#%%
#Os índices das series funcionam das mesma forma que dicionários
import pandas as pd
idades = [39, 30, 27, 18, 15, 12, 10]
series_idades = pd.Series(idades)
series_idades
# %%
idades[0]
# %%
series_idades[0]
# %%
idades[-1]
# %%
#series_idades[-1] -> Isso dá errado, pois não tenho um índice "-1"
series_idades = series_idades.sort_values()
print(series_idades[0])#Você pega pelo índice 
print(series_idades.iloc[0])#Você pega pela posição, independente do índice
# %%
print(series_idades.iloc[-1])#Isso funciona, pois estou pegando pela posição
# %%
nome = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin"]
posicao = ["Capitão", "Combatente", "Navegadora", "Atirador", "Cozinheiro", "Médico", "Arqueóloga"]
series_nome = pd.Series(nome, index=posicao)
series_nome
# %%
print(series_nome["Cozinheiro"])#Pega pelo índice
print(series_nome.iloc[4])#Pega pela posição
# %%
# Podemos ainda criar uma series com dois indices iguais
idades = [39, 30, 27, 18, 15, 12, 10]
posicao = ["Membro", "Membro", "Membro", "Membro", "Membro", "Membro", "Membro"]
series_idades = pd.Series(idades, index=posicao)
series_idades["Membro"]#Retorna todos os membros com esse índice
# %%
#Podemos usar o método .loc para pegar um índice específico mesmo que ele esteja repetido
series_idades.loc["Membro"]
# %%
