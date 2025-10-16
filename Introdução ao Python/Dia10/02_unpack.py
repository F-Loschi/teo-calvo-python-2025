#%%
#Padrão
'''
Ideia de inverter valores sem ter que usar uma variável auxiliar
'''
a = 1
b = 5
print(f"Inicial a = {a}")
print(f"Inicial b = {b}")
c = a
a = b
b = c
print(f"Final a = {a}")
print(f"Final b = {b}")
#%%
# Com unpack
print(f"Inicial a = {a}")
print(f"Inicial b = {b}")
a, b = b, a
print(f"Final a = {a}")
print(f"Final b = {b}")
# %%
#Desempacotamento com *
'''
Aqui o * serve para desempacotar o que sobrar
'''
a, b = 1, 5
#a, b = 1, 2, 3, 4, 5, 6 -> Erro
a, b, *c = 1, 2, 3, 4, 5, 6
print(a)
print(b)
print(c)
# %%
