#%%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv', sep = ';')
df
# %%
df.to_csv("../Dia02/clientes_exportados.csv", index=False)
# %%
df.to_parquet("../Dia02/clientes_exportados.parquet", index=False)
# %%
df.to_excel("../Dia02/clientes_exportados.xlsx", index=False)
# %%
df_3 = pd.read_parquet("../Dia02/clientes_exportados.parquet")
df_3
# %%
df_4 = pd.read_excel("../Dia02/clientes_exportados.xlsx")
df_4
# %%
