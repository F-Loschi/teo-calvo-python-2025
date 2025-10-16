#%%
import pandas as pd
#%%
#Series é melhor que listas por possuir mais funcionalidades
#Mas diferente de listas, Series são unidimensionais
#Identifica o tipo de dado automaticamente
#Exemplo 1 - Criando uma Series a partir de uma lista
idades = [39, 30, 27, 18, 15, 12, 10]
series_idades = pd.Series(idades)
series_idades
# %%
media = series_idades.mean()
media
variancia = series_idades.var()
variancia
desvio_padrao = series_idades.std()
desvio_padrao
# %%
summary = series_idades.describe()
summary
# %%
