import requests as rq
import os 

cidade = "Americana"
api_key = "72d506180e0cdaf12af56a128bb693c6"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

dados = rq.get(url)

resposta = dados.json()

temperatura_atual = resposta['main'] ['temp']
umidade = resposta['main'] ['humidity']

descricao = resposta['weather'] [0]['description']

print(temperatura_atual)
print(umidade)
print(descricao)
