#%%
import pandas as pd
# %%
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep = ';')
transacao_produto.head()
# %%
produtos = pd.read_csv("../../data/produtos.csv", sep = ';')
produtos.head()
# %%
cliente_transacao_produto = transacoes.merge(transacao_produto, on=['IdTransacao'],how = 'left')[['IdTransacao', "IdCliente", "IdProduto"]]
#%%
produtos.dtypes
# %%
cliente_transacao_produto.dtypes
# %%
produtos['IdProduto'] = produtos['IdProduto'].astype('object')
# %%
produtos.dtypes
# %%
df_full = cliente_transacao_produto.merge(produtos, on=['IdProduto'], how='left')
#%%
df_full
# %%
(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)
# %%
