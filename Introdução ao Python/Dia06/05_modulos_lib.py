#%%
def sqrt(numero):
    return numero ** 0.5
#Mas eu preciso ficar criando várias funções matemáticas?
#Não, podemos importar o módulo math que já vem com o Python
#%%
import math
# %%
math.sqrt(25)
math.factorial(5)
math.pow(2, 3)
math.e
math.pi
# %%
#Podemos importar apenas uma função específica do módulo
from math import sqrt, factorial
# %%
#Podemos ainda importar uma biblioteca com um nome diferente
import math as m