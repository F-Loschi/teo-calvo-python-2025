#%%
def juros_compostos(valor_inicial:int, taxa_juros:float, anos:float)->float:
    #Isso chama docstring
    '''
    Calcula o montante de uma aplicação financeira com juros compostos.

    param valor_inicial: 
        Valor inicial da aplicação

    param taxa_juros: 
        Taxa de juros (em decimal, ex: 0.13 para 13%)
    
    param anos: 
        Número de anos da aplicação
    '''
    return valor_inicial * (1 + taxa_juros) ** anos
# %%
juros_compostos(1000, 0.13, 4)
# %%
# Dá ruim se passar os parâmetros fora de ordem
juros_compostos(4, 0.13, 1000)
# %%
# Podemos usar parâmetros nomeados
juros_compostos(taxa_juros=0.13, anos=4, valor_inicial=1000)
# %%
