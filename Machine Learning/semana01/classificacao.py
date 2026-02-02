#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%

df = pd.read_excel('../data/dados_cerveja_nota.xlsx')
df.head()
# %%
df['aprovado'] = (df['nota'] >= 5).astype(int)
df.tail()
# %%
plt.plot(df['cerveja'], df['aprovado'], 'royalblue', marker='o', linestyle='None')
plt.grid(True)
plt.title("Relação Cerveja vs. Aprovado")
plt.xlabel("Cerveja")
plt.ylabel("Aprovado (0 = Não, 1 = Sim)")
# %%
from sklearn import linear_model

reg = linear_model.LogisticRegression(penalty=None, fit_intercept=True)
#%%
reg.fit(df[['cerveja']], df['aprovado'])
reg_predict = reg.predict(df[['cerveja']].drop_duplicates())
reg_predict_proba = reg.predict_proba(df[['cerveja']].drop_duplicates())[:, 1]


# %%
from sklearn import tree

arvore_full = tree.DecisionTreeClassifier(random_state=42)
arvore_full.fit(df[['cerveja']], df['aprovado'])
arvore_full_predict = arvore_full.predict(df[['cerveja']].drop_duplicates())
arvore_full_predict_proba = arvore_full.predict_proba(df[['cerveja']].drop_duplicates())[:, 1]
# %%
plt.figure(dpi=400)
plt.plot(df['cerveja'], df['aprovado'], 'royalblue', marker='o', linestyle='None')
plt.grid(True)
plt.title("Relação Cerveja vs. Aprovado")
plt.xlabel("Cerveja")
plt.ylabel("Aprovado (0 = Não, 1 = Sim)")
plt.hlines(0.5, xmin = 1, xmax = 9, color='red', linestyle='--')
plt.plot(df[['cerveja']].drop_duplicates(), reg_predict, color='orange')
plt.plot(df[['cerveja']].drop_duplicates(), reg_predict_proba, color='green')

plt.plot(df[['cerveja']].drop_duplicates(), arvore_full_predict, color='red')
plt.plot(df[['cerveja']].drop_duplicates(), arvore_full_predict_proba, color='magenta')

plt.legend(['Observado',
            'Predito Regressão(Classe)',
            'Predito Regressão(Probabilidade)',
            'Predito Árvore(Classe)',
            'Predito Árvore(Probabilidade)'])
# %%
arvore_d2 = tree.DecisionTreeClassifier(random_state=42, max_depth=2)
arvore_d2.fit(df[['cerveja']], df['aprovado'])
arvore_d2_predict = arvore_d2.predict(df[['cerveja']].drop_duplicates())
arvore_d2_proba = arvore_d2.predict_proba(df[['cerveja']].drop_duplicates())[:,1]
# %%
from sklearn import naive_bayes
nb = naive_bayes.GaussianNB()
nb.fit(df[['cerveja']], df['aprovado'])
nb_predict = nb.predict(df[['cerveja']].drop_duplicates())
nb_proba = nb.predict_proba(df[['cerveja']].drop_duplicates())[:,1]
#%%
plt.figure(dpi=400)
plt.plot(df['cerveja'], df['aprovado'], 'o', color='royalblue')
plt.grid(True)
plt.title("Cervaja vs Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovado")
plt.plot(df['cerveja'].drop_duplicates(), reg_predict, color='tomato')
plt.plot(df['cerveja'].drop_duplicates(), reg_predict_proba, color='red')

plt.plot(df['cerveja'].drop_duplicates(), nb_predict, color='green')
plt.plot(df['cerveja'].drop_duplicates(), nb_proba, color='magenta')

plt.plot(df['cerveja'].drop_duplicates(), arvore_d2_predict, color='blue')
plt.plot(df['cerveja'].drop_duplicates(), arvore_d2_proba, color='black')

plt.hlines(0.5, xmin=1, xmax=9, linestyles='--', colors='black')

plt.legend(['Oberservação',
            "Reg Predict",
            "Reg Proba",
            "Naive Bayes Predict",
            "Naive Bayes Proba",
            "Árvore D2 Predict",
            "Árvore D2 Proba",
            ])
# %%
