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
    print(linhas.strip("\n").split(";"))
# %%
