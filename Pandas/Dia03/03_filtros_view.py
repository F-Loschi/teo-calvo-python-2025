#%%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
#%%
filtro = clientes['qtdePontos'] == 0

clientes[filtro]
# %%
#Agora o interessante:
clientes_sem_pontos = clientes[filtro]

clientes_sem_pontos['FlagClienteSemPontos'] = True

clientes_sem_pontos.head()
#Aviso: SettingWithCopyWarning, o que indica que estamos criando uma cópia dos dados
#Isso pode gerar problemas se tentarmos modificar os dados originais, 
#podemos pensar no filtro usado como uma "view" dos dados originais, ou seja, ela
#funciona como um ponteiro que aponta para os dados originais que passam pelo filtro
# %%
