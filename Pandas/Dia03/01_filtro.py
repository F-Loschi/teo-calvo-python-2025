#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
# %%
#Filtrando:
#Fazendo um filtro para selecionar apenas as linhas onde a coluna 'QtdePontos' é maior que 1000
#df['QtdePontos']>1000  #Retorna uma série booleana, esse é o filtro
#Aplicando o filtro no DataFrame:
df[df['QtdePontos']>1000]
#IMPORTANTE:
# O filtro pode ser salvo em uma variável para reutilização
# O filtro usado deve ser uma série booleana com o MESMO TAMANHO do DataFrame original
# %%
#Aplicando em outro exemplo:
filtro2 = df['QtdePontos'] >= 50
df[filtro2]
# %%
#Outro exemplo com múltiplas condições:
filtro3 = (df['QtdePontos'] >= 50) & (df['QtdePontos'] > 100)
df[filtro3]
# %%
#Funciona também usando o operador *:
filtro4 = (df['QtdePontos'] >= 50) * (df['QtdePontos'] > 100)
df[filtro4]
# %%
#Usando o operador | (ou):
filtro5 = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro5]
# %%
#Funciona também usando o operador +:
filtro6 = (df['QtdePontos'] == 1) + (df['QtdePontos'] == 100)
df[filtro6]
# %%
