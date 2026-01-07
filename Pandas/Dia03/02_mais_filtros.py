#%%
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv', sep=';')
df.head()
# %%
df[(df['IdProduto']=='5') | (df['IdProduto']=='11')]
# %%
#Podemos usar o método .isin() para filtrar múltiplos valores em uma coluna
df[df['IdProduto'].isin(['5','11'])]
# %%
df.info()
# OBS.: A coluna 'IdProduto' está como objeto (string), o que não é o ideal para IDs numéricos
#Podemos converter a coluna para o tipo numérico (inteiro)
#df['IdProduto'] = pd.to_numeric(df['IdProduto'])
#mas isso retorna um erro, pois existem valores que não podem ser convertidos para número
#Logo, seria preciso fazer um tratamento prévio nesses dados
#o que é mais complexo e foge do escopo atual
# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
#%%
filtro = clientes['DtCriacao'].notna()
clientes[filtro]
# %%
#Podemos negar o filtro usando o operador ~
filtro2 = ~(clientes['DtCriacao'].notna())
clientes[filtro2]
#Isso não retorna nada pois os dados estão todos preenchidos
# %%