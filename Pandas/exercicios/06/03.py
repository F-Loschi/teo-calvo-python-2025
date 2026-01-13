#%%
#06.03 - Qual usuário teve maior quantidade de pontos debitados?
import pandas as pd
# %%
clientes = pd.read_csv('../../data/clientes.csv', sep = ';')
clientes
# %%
clientes.groupby('idCliente').sum().sort_values('qtdePontos', ascending=False).head(1)
# %%
