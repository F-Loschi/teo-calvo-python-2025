#%%
import pandas as pd
import numpy as np
#%%
# 05.01 - Crie uma coluna nova “twitch_points” que á
# resultado da multiplicação do saldo de pontos e a marcação da twitch
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
clientes['twitch_points'] = clientes['flTwitch'] * clientes['qtdePontos']
clientes.head()
#%%
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
clientes['logPontos'] = np.log(clientes['qtdePontos']+1)
clientes.head()
#%%
# 05.03 - Crie uma coluna que sinalize se a
# pessoa tem vínculo com alguma (qualquer uma)
# plataforma de rede social.
clientes['alguma_rede_social'] = clientes['flEmail'] + clientes['flTwitch'] + clientes['flYouTube'] + clientes['flBlueSky'] + clientes['flInstagram']
clientes.head()
#%%
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos?
clientes.sort_values(by='qtdePontos', ascending = False)['idCliente'].head(1)
#%%
# E o menor?
clientes.sort_values(by='qtdePontos')['idCliente'].head(1)
# %%
#05.05 - Selecione a primeira transação diária de cada cliente.
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
transacoes['DtCriacao'] = pd.to_datetime(transacoes['DtCriacao'])
#%%
transacoes = transacoes.sort_values(by=['DtCriacao'])
transacoes.head()
# %%
primeiras_transacoes = transacoes.drop_duplicates(subset=['IdCliente'], keep='first')
primeiras_transacoes
# %%
