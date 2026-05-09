print("-" * 60)
print("Bem vindo a sala de interrogatório, nosso detective fará umas perguntas para nossa investigação")

print("-" * 60)

nome= input("antes de começarmos poderia me informar seu nome:")
relacaoV = input("certo, e qual seria sua relação com a vitima?")
print("Entendi, vamos começar com a primeira pergunta ")
pergunta_um = input("Onde você estava ontem á noite? ") # input recebe dados do teclado do usuário 
pergunta_dois = input("O que você estava fazendo entre 19h e 20h30?")
pergunta_tres = input("Alguém pode confirmar o seu alíbe?")


print (f"Relatório do suspeito(a) {nome} a quem era {relacaoV}da vitima, que no dia do crime relatou estar {pergunta_um} enquanto estava {pergunta_dois}. De acordo com seu relato: '{pergunta_tres} pode confirmar o meu alíbe'") 

