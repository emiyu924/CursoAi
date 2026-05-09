
print ("\tBem vindo a calculadora de médias!")
nota_um = float(input("Digite a primeira nota do aluno:"))
nota_dois= float(input("Digite a segunda nota do aluno:"))
nota_tres= float(input("Digite a terceira nota do aluno:"))
nota_quatro= float(input("Digite a quarta nota do aluno:"))

media = (nota_um + nota_dois + nota_tres + nota_quatro) /4

print (f"a média desse aluno é {media}")

if  media >= 6:
    print("Parabéns o aluno foi aprovado!")

else:
    print("O Aluno está reprovado! Comunique a ele as más notícias")
