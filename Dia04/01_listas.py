#%%
''' Listas do python não são arrays,
mas conseguem guardar qualquer tipo de
dados dentro dela.
Não é porque eu estou guardando um tipo específico
dentro dela que ela vai ser desse tipo.
'''
felipe = ['Felipe', 'Loschi', 18, 0.1, 'Oi', False]
print(felipe[0])
print(felipe[3])
# %%
idades = [28, 42, 43, 15, 20, 32]
print(f"Soma das idades = {sum(idades)}")
print(f"Quantidade de idades = {len(idades)}")
print(f"Média das idades = {sum(idades)/len(idades)}")
print(f"Maior idade = {max(idades)}")
print(f"Menor idade = {min(idades)}")
# %%
pouso_alegre = [846.8, 847.1, 846.5, 846.9, ['Brasil', 'Minas Gerais', 'Sudeste', 'Sul de Minas', 'América'], ['Livia', 'Gavião', 'Tomatinho']]
print(f"Tamanho da lista = {len(pouso_alegre)}")
print(f"Vereador 1 = {pouso_alegre[4][0]}")
#Mesma coisa que:
vereadores = pouso_alegre[4]
vereador1 = vereadores[0]
print(f"Vereador 1 = {vereador1}")
# %%
tamanho = len(pouso_alegre)
pos = tamanho - 1
print(f"Último elemento = {pouso_alegre[pos]}")
pouso_alegre[len(vereadores)-1]
#Mesma coisa que:
print(f"Último elemento = {pouso_alegre[-1]}")
print(f"Penúltimo elemento = {pouso_alegre[-2]}")
# %%
# Slicing
print(f"Do início até o 4º elemento = {pouso_alegre[0:4]}")
print(f"Posições geográficas = {pouso_alegre[4][-2:]}")
# %%
#pouso_alegre[starting:ending:step]
print(f"Vereadores ao contrário = {pouso_alegre[5][::-1]}")
# %%
