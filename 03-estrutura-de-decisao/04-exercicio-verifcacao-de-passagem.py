# Programa: Verificação de passagem

# Faça um programa em Python que peça a idade de uma pessoa
# e verifique se ela paga passagem inteira ou meia passagem.

# Idade menor ou igual a 12 → Meia passagem
# Idade maior que 12 → Passagem inteira

# Receber idade do passgeiro
idade = int(input("Digite sua idade: "))

# Verifica se o passageiro paga meia ou inteira
if (idade <= 12):
    print("O passageiro paga meia passagem")
else:
    (idade >= 12)
    print("O passageiro paga inteira")