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
# Escrevendo em um arquivo
txt = "Era uma vez um menino chamado João que morava em uma pequena vila.\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, "w", encoding="utf-8") as open_file:
    open_file.write(txt)
# %%
# Adicionando texto em um arquivo
with open(nome_arquivo, "a", encoding="utf-8") as open_file:
    open_file.write("Ele adorava explorar a floresta próxima à sua casa.\n")