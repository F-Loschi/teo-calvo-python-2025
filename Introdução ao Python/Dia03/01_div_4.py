#%%
#Um número é divísivel por 4 quando o resto da divisão por 4 é 0
#Quais números entre 4 e 100 são divísiveis por 4?

count = 4
while count <= 100:
    if count % 4 == 0:
        print(count)
    count += 1
# %%
