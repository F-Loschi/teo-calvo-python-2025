#%%
import pandas as pd
# %%
transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.columns = [
    'IdCliente',	
    'flEmail',
    'flTwitch',	
    'flYouTube',
    'flBlueSky',	
    'flInstagram',
    'qtdePontos',
    'DtCriacao',	
    'DtAtualizacao'
]
clientes.head()
# %%
transacoes.merge(right=clientes, how='left', on='IdCliente')
#A linha acima faz a junção dos dois dataframes, retornando apenas as linhas que possuem correspondência em ambos os dataframes com base na coluna 'IdCliente'.
# %%
transacoes.merge(
    right = clientes,
    how = 'left',
    on = ['IdCliente'],
    suffixes=['Transacao', 'Cliente']
)
#O merge acima faz a junção dos dois dataframes, retornando todas as linhas do dataframe 'transacoes' e adicionando as colunas do dataframe 'clientes' onde houver correspondência na coluna 'IdCliente'. As colunas que possuem o mesmo nome em ambos os dataframes recebem sufixos diferentes para diferenciá-las.
# %%
df_1 = pd.DataFrame({
    "transacao": [1,2,3,4,5],
    "nome": ["t1", "t2", "t3", "t4", "t5"],
    "idCliente": [1,2,3,2,2],
    "valor": [10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "nome": ["teo", "nah", "mah", "jose"],
})
# %%
df_1.merge(df_2, left_on=['idCliente'], right_on=['id'], how='left', suffixes=['Transacoes', 'Clientes'])
# %%
