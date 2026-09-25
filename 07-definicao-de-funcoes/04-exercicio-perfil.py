# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
plano = input("Digite o seu tipo de plano: ")

def exibir_perfil(nome, idade, plano):
    perfil = (f"nome", {nome}, "Idade", {idade}, "plano", {plano})
    print(perfil)