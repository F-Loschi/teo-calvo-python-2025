#%%
import pandas as pd
nome = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin"]
idade = [39, 30, 27, 18, 15, 12, 10]
altura = [1.72, 1.81, 1.70, 1.74, 1.77, 0.90, 1.88]
cargo = ["Capitão", "Combatente", "Navegadora", "Atirador", "Cozinheiro", "Médico", "Arqueóloga"]
series_nome = pd.Series(nome)
series_idade = pd.Series(idade)
#%%
df = pd.DataFrame()
df['Nome'] = series_nome
df['Idade'] = series_idade
df['Altura'] = altura
df['Cargo'] = cargo
df
# %%
df['Cargo']
# %%
#Podemos acessar uma linha específica usando o .loc ou o .iloc
print(type(df.loc[3]))
df.iloc[3]#Acessa a linha na posição 3
# %%
#Podemos acessar uma coluna específica de uma linha que foi acessada com o .iloc e o .loc
df.iloc[3]['Cargo']
# %%
