valor_compra = float(input("Digite o valor da compra: R$"))

# Verifica se a idade é maior que 18
if valor_compra > 500:
    desconto = 30
    print(f"PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE {desconto}")
elif valor_compra >= 250:
    desconto = 10
    print(f"PARABÉNS. VOCÊ GANHOU {desconto}% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
else:
    desconto = 0
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")