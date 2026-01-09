#%%
import pandas as pd
import numpy as np
# %%

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
# %%
df['100Pontos+'] = df['qtdePontos']+100
# %%
#Para saber se ele tem um email ou twitch
df['email_twitch'] = df['flEmail'] + df['flTwitch']
df
# %%
#Para saber se ele tem um email e twitch
df['email_twitch'] = df['flEmail'] * df['flTwitch']
df
# %%
