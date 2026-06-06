import requests as rq

url = "https://api.exchangerate-api.com/v4/latest/BRL"

dados = rq.get(url)

resposta = dados.json()

valor_moeda_base = resposta ['rates'] ['BRL']

euro = 1 / resposta ['rates'] ['EUR']
dolar = 1 / resposta ['rates'] ['USD']

print (f" {euro:.2f} BRL = 1 EUR")
print (f" {dolar:.2f} BRL = 1 USD")