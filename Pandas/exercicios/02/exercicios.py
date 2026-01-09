#%%
import pandas as pd
# %%
#Leia o arquivo transacoes.csv com a formatação correta;
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
#Adicione uma coluna com valores 1
transacoes['valores'] = 1
transacoes.head()
# %%
#Salve o dataframe com nome: transacoes_1.csv
transacoes.to_csv('transacoes_1.csv', index=False)