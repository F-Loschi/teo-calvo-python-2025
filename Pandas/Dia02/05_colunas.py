#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
df.rename(columns = {'QtdePontos': 'QtPontos'}, inplace=True)#método para renomear colunas do dataframe, onde columns é o parâmetro que recebe um dicionário com o nome antigo como chave e o novo nome como valor, e inplace=True faz a alteração no próprio dataframe
df.columns
# %%
df['IdCliente']#seleciona a coluna IdCliente do dataframe
# %%
df[['IdCliente', 'QtPontos']]#seleciona as colunas IdCliente e QtPontos do dataframe
# %%
colunas = list(df.columns)#cria uma lista com o nome das colunas do dataframe
colunas.sort()#ordena a lista em ordem alfabética
colunas
# %%
df = df[colunas]#reorganiza as colunas do dataframe de acordo com a lista colunas
df
# %%
