#%%
# Escrevendo em um arquivo
txt = "Era uma vez um menino chamado João que morava em uma pequena vila.\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, "w", encoding="utf-8") as open_file:
    open_file.write(txt)
# %%
# Adicionando texto em um arquivo
with open(nome_arquivo, "a", encoding="utf-8") as open_file:
    open_file.write("Ele adorava explorar a floresta próxima à sua casa.\n")