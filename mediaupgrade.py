listaNotas = []

print("-" * 50)
print("\tBem vindo ao I.A que calcula notas e média final do aluno!")
print("\tPara começarmos entre com seu login")

nomeUser= input("Digite o seu nome:")
senhaUser = input("Digite a sua senha:")

if nomeUser == "professor" and  senhaUser == "4321":
    print ("Acesso liberado! Bem vindo de volta")
    while True:
        notas = (input("Digite a nota que deseja inserir (Escreva pare para parar)"))
        if notas.lower()== "pare":
             break
        else:
            listaNotas.append(float(notas))
        
    media = sum (listaNotas) / len (listaNotas)

    print(f"A media final do Aluno é {media:.2f}") 

    if  media >= 6:
         print("Parabéns o aluno foi aprovado!")

    else:
            print("O Aluno está reprovado! Comunique a ele as más notícias")
else:
     print("Acesso negado! Verifique as informações de login e tente novamente!")
        
        
