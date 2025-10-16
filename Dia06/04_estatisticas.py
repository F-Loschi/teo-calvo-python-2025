#%%
def soma(a: float, b: float) -> float:
    '''
    Retorna a soma de dois números.
    '''
    return a + b

def media(a: float, b: float) -> float:
    '''
    Retorna a média de dois números.
    '''
    return soma(a,b)/ 2
#%%
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"A média entre {a} e {b} é {media(a,b)}")
# %%
