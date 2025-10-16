#%%
import os

# Muda o diretório de trabalho para onde o script está
if '__file__' in globals():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("✅ Trabalhando em:", os.getcwd())
arquivo = "data.csv"

with open(arquivo, "r", encoding="utf-8") as open_file:
    # Lê todas as linhas do arquivo
    data = open_file.readlines()

for linhas in data:
    print(linhas)
# %%

dados = dict()

chaves = data[0].strip().split(";")
print(chaves)
for c in chaves:
    dados[c] = []

for linhas in data[1:]:
    valores = linhas.strip("\n").split(";")
    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])