#%%
import pandas as pd
import requests#Usado para tratar o erro de requisição que o wikipedia gera


url = "https://pt.wikipedia.org/wiki/unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)

print(len(dfs))
# %%
uf = dfs[1]
# %%
uf.dtypes
# %%
def str_to_float(x:str):
    x = (x.replace(" ", "")
        .replace(",", ".")
        .replace("\xa0", ""))
    return float(x)
# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)

uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)

uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
# %%
def expectativa_to_anos(x):
    x = x.replace(" anos", "").replace(",", ".")
    return float(x)

def alfabetizacao_to_percentual(x):
    x = x.replace("%", "").replace(",", ".")
    x = float(x)
    return (x/100)

def mortalidade_to_percentual(x):
    x = x.replace("‰", "").replace(",", ".")
    x = float(x)
    return (x/1000)
# %%
uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(expectativa_to_anos)
uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(alfabetizacao_to_percentual)
uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_percentual)
#%%
uf.head()
# %%
uf.dtypes
# %%
def uf_to_regiao(uf):

    # tartar uf
    # uf = uf

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
# %%
uf
# %%
def classifica_bom(linha):
    if (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016)"] < 15 and 
            linha["IDH (2010)"] > 700):
        return "Bom"
    return "Preocupante"

uf["Parece bom?"] = uf.apply(classifica_bom, axis=1)
# %%
uf
# %%
