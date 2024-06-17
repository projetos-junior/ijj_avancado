# Capturando e convertendo os dados do usuário diretamente no input
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
idade = int(input("Digite sua idade: "))

# Capturando as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Variável com o valor somado da altura e idade
soma_altura_idade = altura + idade

# Calculando a média das notas
media_notas = (nota1 + nota2 + nota3) / 3

# Imprimindo os dados na tela
print(f"O nome do usuario é {nome}, Altura: {altura} metros, Idade: {idade} anos, a Soma da altura e idade é {soma_altura_idade} e a médiada das nota são {media_notas:.2f}")