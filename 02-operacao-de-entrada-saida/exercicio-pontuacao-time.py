# Entrada de dados
time = input("Insira o nome do time: ")
vitorias = int(input("Quantidade de vitorias: "))
empates = int(input("Quantidade de empates: "))

# Processamento computacional
valor_vitoria = vitorias * 3
valor_empates = empates
total_do_time = valor_vitoria + valor_empates  

# Saída de informações
print(f"O {time} venceu {vitorias} e empatou {empates} chegando ao total de {total_do_time} pontos")