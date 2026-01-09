#%%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv', sep = ';')
df.head()
# %%
def get_last_id(name):
    return name.split('-')[-1]
# %%
id_novo = []

for i in df['idCliente']:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()
# %%
# Essa forma demonstrada acima é a mais trabalhosa de se fazer.
#Comumente, usa-se o método "apply" do pandas que aplica algo
#elemento a elemento:
df["idCliente"].apply(get_last_id)
#Com esse comando, aplicamos a função "get_last_id" na coluna 
#"idCliente" elemento a elemento, como pode ser visto
# %%
