#%%
import os

# Muda o diretório de trabalho para onde o script está
if '__file__' in globals():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("✅ Trabalhando em:", os.getcwd())

nome_arquivo = "historia.txt"
#Abre o arquivo em modo de leitura
#Jeito não usual:
#open_file = open(nome_arquivo, "r", encoding="utf-8")
#conteudo = open_file.read()
#print(conteudo)
#Fecha o arquivo
#open_file.close()

#Jeito usual (com gerenciador de contexto)
with open(nome_arquivo, "r", encoding="utf-8") as open_file:
    conteudo = open_file.read()
    print(conteudo)

# %%
