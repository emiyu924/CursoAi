import requests as rq

#Para criar uma função, utilizamos o comando def
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    try:
       dados = rq.get(url)
       resposta = dados.json()
       valor_moeda_base = resposta ['rates'] ['BRL']
       euro = 1 / resposta ['rates'] ['EUR']
       dolar = 1 / resposta ['rates'] ['USD']
       return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} = 1 BRL"

    except:
        return("Não foi possivel realizar a conversão de valores")
    
print(get_moedas())