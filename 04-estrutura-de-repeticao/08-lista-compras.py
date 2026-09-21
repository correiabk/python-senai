compras = []

produto = input("Diite um produto (ou 'Fim' para terminar): ")

while produto != "Fim":
    compras.append(produto)

    produto = input("Digite outro produto (ou 'Fim' para terminar): ")

    print(compras)
    print("Lista de compras:")

for lista_produto in compras:
    print('-', lista_produto)