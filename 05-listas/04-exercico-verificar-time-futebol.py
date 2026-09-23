# Crie um programa em Python que tenha uma lista com alguns times de futebol.

# Peça para o usuário digitar o nome de um time.

# Verifique se o time digitado está na lista.

# Se estiver, mostre:
# "Esse time está na lista!"

# Caso contrário, mostre:
# "Esse time não está na lista!"


times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]

team = input("Insira o nome do sue time em: ")

if team in times:
    print(f"{team} está na lista!")
else:
    print(f"{team} não está na lista!")