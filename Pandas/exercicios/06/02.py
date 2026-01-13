#%%
#06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
import pandas as pd
# %%
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
transacoes.groupby(by='IdCliente').count().sort_values(by='QtdePontos',ascending=False).head(10)
# %%
