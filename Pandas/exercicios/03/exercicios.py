#%%
import pandas as pd
# %%
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
#03.01 - Quantas linhas há no arquivo clientes.csv ?
print(f"Número de linhas no arquivo clientes.csv: {len(clientes)}")
# %%
#03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
#%%
transacoes.dtypes
# %%
#03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
df_produtos = pd.read_csv("../../data/produtos.csv", sep = ';')
df_produtos.dtypes

# %%
#03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
#clientes['idCliente'][4]
clientes.iloc[4]['idCliente']
# %%
#03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar)
#  do arquivo clientes.csv ?
#clientes['qtdePontos'][9]
clientes.iloc[9]['qtdePontos']
# %%
