# Programa para calcular a média de 4 notas

nome = input("Por favor, digite seu nome: ")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f"Olá, {nome}! Sua média é: {media:.2f} pontos")