#%%
import pandas as pd

# %%
df = pd.read_parquet("../data/dados_clones.parquet")
df.head()
# %%
df_defeituoso = df[df['Status ']=='Defeituoso']
# %%
df_defeituoso.groupby('General Jedi encarregado').count()
#Se fizessemos uma decisão baseada apenas no número de clones defeituosos, os generais Yoda 
#e Shaak Ti seriam demitidos, uma vez que todos os clones que apresentam defeitos estam sob o
#comando deles.
# %%
#Porém, vamos olhar para a árvore de decisão que foi treinada com esses dados:
from sklearn import tree
# %%
model = tree.DecisionTreeClassifier()
# %%
df['Status '].unique()
# %%
df = df.replace({
    'Yoda' : 0, 'Shaak Ti' : 1, 'Obi-Wan Kenobi' : 2, 'Aayla Secura' : 3, 'Mace Windu' : 4,
    'Tipo 1' : 1, 'Tipo 2' : 2, 'Tipo 5' : 5, 'Tipo 3' : 3, 'Tipo 4' : 4
})
# %%
df.info()
# %%
df.columns
# %%
x = df[['Massa(em kilos)', 'Estatura(cm)']]
y = df['Status ']
#%%
y
# %%
model.fit(x,y)
#%%
features = ['Massa(em kilos)', 'Estatura(cm)']    
# %%
import matplotlib.pyplot as plt
#%%
plt.figure(dpi=400)

tree.plot_tree(model, feature_names=features,
               class_names=model.classes_,
               filled=True,
               max_depth=3
)
#Olhando pela árvore de decisão, percebemos que na verdade pode haver uma ligação entre os clones defeituosos
#e suas medidas físicas, o que muda completamente a análise anterior.
# %%
