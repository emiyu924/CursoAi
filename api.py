#instalar bibliotecas
#pip install requests

#importar/adicionar ao código

import requests 

nome = input("Digite o seu nome:")
email = input("Digite o seu e-mail:")
telefone = input("Digite o seu telefone:")
idade = input("Digite a sua idade:")
cep = input("Digite o cep que gostaria de verificar:")

# utilizamos o f string para conseguir inserir uma variável no link 

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json() 

print (f"Bem vindo ao Mercado Livre {nome}! O seu e-mail é {email}. O seu telefone é{telefone} e sua idade é {idade} anos, Você mora na {dados['logradouro']} na cidade {dados['localidade']} no estado de {dados['estado']}. ")



# atribuindo variáveis para cada um dos resultados
# rua = dados['logradouro']
# bairro = dados['bairro']
# localidade = dados['localidade']

# print(rua)
# print(bairro)
# print(localidade)
 

