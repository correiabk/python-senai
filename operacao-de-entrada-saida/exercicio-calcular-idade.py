# Faça um programa que peça o ano de nascimento de uma pessoa e calcule a sua idade atual.
# Depois, mostre o ano de nascimento e a idade no terminal.

# Entrada de dados
anonasc = int(input("Insira o seu ano de nascimento: "))
anoatu = int(input("Insira o ano atual: "))

# Processamento de dados
idadeat = anoatu - anonasc

# Saída de informações
print(F"Você nasceu no ano de {anonasc} e tem {idadeat} anos")