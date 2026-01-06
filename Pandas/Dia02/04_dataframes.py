#%%
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep=';')
df_clientes
# %%
df_clientes.head()#esse comando mostra o cabeçalho do dataframe
# %%
df_clientes.tail()#esse comando mostra o final do dataframe
# %%
df_clientes.shape#é um atributo que mostra a quantidade de linhas e colunas do dataframe
# %%
df_clientes.columns#é um atributo que mostra o nome das colunas do dataframe
# %%
df_clientes.index#é um atributo que mostra o índice do dataframe
# %%
df_clientes.info(memory_usage='deep')#é um método que mostra informações sobre o dataframe
# %%
df_clientes.dtypes#é um atributo que mostra os tipos de dados das colunas do dataframe
# %%
