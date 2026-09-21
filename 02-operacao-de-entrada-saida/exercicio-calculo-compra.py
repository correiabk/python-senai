# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados
produto = input("Qual o produto comprado?: ")
preco = float(input("Insira o preço do produto: "))
unid = int(input("Quantidade de unidades adquiridas: "))

# Processamento de dados
compra = unid * preco

# Saída de informações
print(f"Você comprou {unid} unidades de {produto} pagando ao total R${compra:.2f}")
