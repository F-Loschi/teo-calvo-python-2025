#%%
import pandas as pd

df = pd.read_excel('../data/dados_cerveja.xlsx')
df.head()
# %%
df.columns
# %%
features = ['temperatura', 'copo', 'espuma', 'cor']
x = df[features]
y = df['classe']
x
# %%
from sklearn import tree

model = tree.DecisionTreeClassifier()
#%%
model.fit(x, y)
# Isso aqui dá bosta pois temos coisas no nosso dataset que não são números ou então não são convertíveis para números
# %%
x = x.replace({
    'mud' : 1, 'pint' : 2,
    'sim' : 1, 'não' : 0,
    'clara' : 0, 'escura' : 1
})
x
# %%
model.fit(x, y)
#Agora, após propriamente mudar as características para valores numéricos, conseguimos treinar o modelo
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(model, feature_names=features,
               class_names=model.classes_,
               filled=True
)
# %%
