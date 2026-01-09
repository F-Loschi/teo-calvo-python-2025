#%%
import pandas as pd
# %%
#04.01 - Quantos clientes tem vínculo com a Twitch?
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
clientes[clientes['flTwitch']==1]['flTwitch'].shape[0]
# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
clientes[clientes['qtdePontos']>1000].shape[0]
# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
#%%
pd.to_datetime(transacoes['DtCriacao'])
transacoes[(transacoes['DtCriacao'] >= '2025-02-01')*(transacoes['DtCriacao'] < '2025-02-02')].shape[0]
# %%
