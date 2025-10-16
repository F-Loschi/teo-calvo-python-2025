#%%
def parOuImpar(numero:int):
    '''
    Função que verifica se um número é par ou ímpar.

    Parâmetros:
        numero: int - número a ser verificado

    Retorno:
        Não há retorno, apenas printa se o número é par ou ímpar.
    '''
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

#%%
parOuImpar(10)
parOuImpar(7)

# %%
