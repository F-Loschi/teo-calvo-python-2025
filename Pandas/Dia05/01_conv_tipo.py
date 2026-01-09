#%%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%
clientes['qtdePontos'].astype(float)
# %%
pd.to_datetime(clientes['DtCriacao'])
#Essa linha era pra ter falhado, mas o novo dataset já está tratado, mas 
#se fosse o antigo, daria erro e colocarei como se tivesse dado erro.
# %%
clientes['DtCriacao'] = clientes['DtCriacao'].replace(
    {'0000-00-00 00:00:00.000': '2025-01-08 23:00:00.000'})
pd.to_datetime(clientes['DtCriacao'])
# %%
