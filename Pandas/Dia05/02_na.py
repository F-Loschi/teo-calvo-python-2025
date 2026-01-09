#%%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%
clientes.dropna(how = 'all')#Significa que pra dropar a linha, todos os valores dela devem ser NaN
clientes.dropna(how = 'any')#Significa que pra dropar a linha, qualquer valor dela ser NaN já é suficiente

# %%
df = pd. DataFrame(
    {
        "nome": ["Teo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None, 5423]
    }
)
#O parâmetro subset indica quais colunas devem ser consideradas na hora de dropar as linhas
df.dropna(how = 'any', subset = ['idade', 'salario'])
#E ele continua levando o 'how' em consideração, logo, se for 'all', só dropa se todas as colunas do subset forem NaN
# %%
#Podemos também preencher os valores NaN com algum valor específico
df.fillna(0) 
# %%
