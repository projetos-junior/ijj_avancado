#USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, imprima na tela "Indivíduo possui idade mínima para dirigir"

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se a idade é maior que 18
if idade > 18:
    print("Indivíduo possui idade mínima para dirigir")
elif 17 <= idade <= 18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print("Indivíduo não possui idade mínima para dirigir")