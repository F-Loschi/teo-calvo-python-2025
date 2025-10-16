#Dict Comprehension
#%%
#Modelo normal que fazia antes:
x = []
for i in range(1,101):
    x.append(i)

x
# %%
#Com o dict:
'''
y -> Nome da lista
[]-> Para criar a lista
Primeiro 'i' -> Valor que vai ser colocado dentro cada vez que o i for iterado
for i in range(1,101) -> For padrão que vai de 1 a 100

'''
y = [i for i in range(1,101)]
y
# %%
#Fazendo uma máscara
def par(x):
    return x%2 == 0

z = [par(i) for i in range(1,101)]
z
# %%
#Aplicando a máscara
'''
Aqui ele vai colocar o número em si mas só se a função retornar true

Só considera o começo se passar o if
'''
w = [i for i in range(1, 101) if par(i)]
w
# %%
