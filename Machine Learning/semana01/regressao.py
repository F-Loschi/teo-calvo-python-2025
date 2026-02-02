#%%
import pandas as pd

df = pd.read_excel('../data/dados_cerveja_nota.xlsx')
df.head()
# %%
from sklearn import linear_model
# Na linha acima importamos a biblioteca de regressão linear do sklearn
from sklearn import tree
X = df[['cerveja']] #Isso é uma matriz(dataframe) com uma única coluna
y = df['nota'] #Isso é um vetor(Series)

#Isso é o MACHINE LEARNING
reg = linear_model.LinearRegression()
reg.fit(X, y) #Aqui estamos treinando o modelo de regressão linear
# %%
b = reg.coef_
# %%
a = reg.intercept_
# %%
predict = reg.predict(X.drop_duplicates())

arvore_full = tree.DecisionTreeRegressor(random_state=42)
arvore_full.fit(X, y)
predict_arvore_full = arvore_full.predict(X.drop_duplicates())

arvore_d2 = tree.DecisionTreeRegressor(random_state=42,
                                       max_depth=2)
arvore_d2.fit(X, y)
predict_arvore_d2 = arvore_d2.predict(X.drop_duplicates())
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

plt.plot(X["cerveja"], y, 'o') #Dados originais
plt.grid(True)
plt.title("Relação Cerveja vs. Nota")
plt.xlabel("Cerveja")
plt.ylabel("Nota")

plt.plot(X.drop_duplicates()['cerveja'], predict)
plt.plot(X.drop_duplicates()['cerveja'], predict_arvore_full, color='green')
plt.plot(X.drop_duplicates()['cerveja'], predict_arvore_d2,color='magenta')


plt.legend(['Observado',
            f'y = {a:.3f} + {b:.3f} x',
            'Árvore Full',
            'Árvore Depth = 2',
            ])
# %%

tree.plot_tree(arvore_full,
               feature_names=['cerveja'],
               filled=True)
# %%
