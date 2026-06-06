import requests as rq

#Para criar uma função, utilizamos o comando def
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
       dados = rq.get(url)
       resposta = dados.json()
       valor_moeda_base = resposta ['rates'] ['USD']
       euro = resposta ['rates'] ['EUR']
       real = resposta ['rates'] ['BRL']
       libras_E = resposta ['rates'] ['GBP']
       pesos_A =  resposta ['rates'] ['ARS']
       
       return f" BRL {real:.2f} = 1 USD | EUR {euro:.2f} = 1 USD | GBP = {libras_E:.2f} = 1 USD | ARS = {pesos_A:.5f} = 1 USD  "

    except:
        return("Não foi possivel realizar a conversão de valores")
    
print(get_moedas())