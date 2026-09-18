# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso

# Entrada de dados
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

# Calculo de imc
imc = peso / (altura * altura)
print(F"Seu IMC É {imc:.2f}")

if imc < 18.5:
    print("Você esta abaixo do peso")
elif imc < 25:
    print("Você esta com o peso normal")
else:
    print("Você está acima do peso")
          
