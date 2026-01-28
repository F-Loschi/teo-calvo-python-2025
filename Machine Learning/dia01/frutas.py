#%%
import pandas as pd
# %%
df = pd.read_excel('../data/dados_frutas.xlsx')
df.head()
# %%
from sklearn import tree
#Na linha acima importamos a biblioteca de árvores de decisão do sklearn
arvore = tree.DecisionTreeClassifier(random_state=42)# O random_state é para garantir que os resultados sejam reprodutíveis
#Na linha acima criamos um classificador do tipo árvore de decisão
#%%
df.columns
# %%
y = df['Fruta'] # Essa é a variável alvo (target)
caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']
x = df[caracteristicas]# Essa é a matriz de características (features)
# %%
# ISSO AQUI É O MACHINE LEARNING
arvore.fit(x, y)# Treinamos o classificador com os dados
# Com isso, a árvore de decisão aprendeu a classificar as frutas que passamos
# %%
arvore.predict([[0,1,0,1]])
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore,
               feature_names=caracteristicas,
               class_names=arvore.classes_,
               filled=True)


# %%
# Podemos ainda prever a probabilidade de cada classe
proba = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(proba, index=arvore.classes_)
# %%
