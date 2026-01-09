#%%
import pandas as pd

# %%
df = pd.DataFrame({
    'nome' : ['Téo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah'],
    'sobrenome' : ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva'],
})
df
# %%
df.drop_duplicates()
# %%
df = pd.DataFrame({
    'nome' : ['Téo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah'],
    'sobrenome' : ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva'],
    'idade' : [23, 25, 43, 22, 26, 28, 29]
})
df

# %%
df = df.sort_values(by='idade', ascending=False)
df.drop_duplicates(subset=['nome', 'sobrenome'])
# %%
