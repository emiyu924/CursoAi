import requests as rq
cidade = "Americana"
api_key = "72d506180e0cdaf12af56a128bb693c6"

def get_clima():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

    try:
        dados = rq.get(url)
        resposta = dados.json()
        temperatura_atual = resposta['main'] ['temp']
        umidade = resposta['main'] ['humidity']
        descricao = resposta['weather'] [0]['description']
        return f"A temperatura atual é {temperatura_atual}, a umidade está {umidade} e a descrição do clima está {descricao}"
    except:
        return("Não foi possivel acessar os dados do clima")
    
print(get_clima())
