#%%
import requests

url = "https://pokeapi.co/api/v2/pokemon/greninja/"

#Para fazer uma requisição, usa-se o get, para pegar alguma coisa.
#Queremos apenas consumir um dado
resposta = requests.get(url)
# %%
print(resposta)
# Possíveis print:
# <Response [200]> -> deu certo
# <Response [404]> -> não encontrou
# <Response [500]> -> deu erro no servidor
# <Response [502]> -> deu erro no servidor
# %%
resposta.text
#Mostra o texto dentro da requisição
resposta.json()
#Assim deixa mais bonito
# %%
dados = resposta.json()
print(type(dados))
# %%
pokemons = [
    "pikachu",
    "squirtle",
    "greninja",
    "vulpix",
    "bulbassur",
    "charmander"
]

url = "https://pokeapi.co/api/v2/pokemon/{pokemon}/"
#Colocar algo entre "{}" se chama "place-holder", que é como um coringa, algo que pode ser alterado
dados = []
for i in pokemons:
    resposta = requests.get(url.format(pokemon=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados
# %%
import json

with open("pokemons.json", "w") as open_file:
    json.dump(dados, open_file, ensure_ascii= False, indent=4)
# %%
