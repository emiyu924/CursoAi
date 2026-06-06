import requests as rq
cep = input("Digite o CEP da sua cidade: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

resposta = dados.json()


print(f"o seu usuário mora na {resposta['logradouro']} no bairro {resposta['bairro']} no estado de {resposta['estado']} na região {resposta['regiao']} ")