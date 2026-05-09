listaNumeros = []
print("\tBem vindo ao I.A que calcula Somas!")

while True:
        numeros = (input("Digite os números que deseja somar (Escreva pare para parar): "))
        if numeros.lower()== "pare":
             break
        else:
            listaNumeros.append(float(numeros))
        
total = sum (listaNumeros) 

print(f"a soma dos números que você inseriu é {total}")
        