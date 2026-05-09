
print("-" * 60)
print("Bem vindo ao formulário de cadastro inicial para abertura de contas")

print("-" * 60)

nome = input("Digite seu nome: ") # input recebe dados do teclado do usuário 
dt_nasc = int(input("Digite o ano do seu nascimento:"))
email = input("Digite seu email: ")
country = input("informe o país de sua residência:")
estado = input("informe o estado da sua residência:")
cidade = input("Por último informe a cidade da sua residência:")
ano_atual = int(input("Informe o ano atual:"))
idade = ano_atual - dt_nasc
print(f"Olá {nome} enviaremos uma confirmação no email cadastrado: {email}, confirme por favor se os dados informados estão corretos: o ano do seu nascimento é {dt_nasc}, Sua cidade é{cidade} em {estado} no {country}. Com base nas suas informações detectamos que sua idade é {idade}") 


