# Cria um programa que percorra os números de 1 a 10 
# e mostre se cada número é par ou ímpar.

for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"O valor {numero} é PAR \n")

    elif numero % 1 == 0:
        print(f"O valor {numero} é IMPAR \n")

    else:
        print("Invalido")