# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

# Digite sua idade
idade = int(input("Digite sua idade: "))

# Validação de idade
if idade >=18:
    print("entrada permitida")
elif idade >= 16:
    print("Entrada acompanhada de responsavel")
else:
    print("Entrada não permitida")