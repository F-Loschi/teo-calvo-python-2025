#%%
#06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
import pandas as pd
# %%
clientes = pd.read_csv('../../data/clientes.csv', sep = ';')
clientes.head()
# %%
clientes['redesSociais'] = (clientes['flEmail'] + 
                          clientes['flTwitch'] + 
                          clientes['flYouTube'] + 
                          clientes['flBlueSky'] +
                          clientes['flInstagram'])

# %%
print(f'Média de redes sociais: {clientes["redesSociais"].mean()}')
print(f'Variância de redes sociais: {clientes["redesSociais"].var()}')
print(f'Máximo de redes sociais: {clientes["redesSociais"].max()}')
# %%
