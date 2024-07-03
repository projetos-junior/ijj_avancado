def verificar_time(matricula):
    if matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

# Exemplo de uso
numero_matricula = int(input("Digite o número de matrícula: "))
verificar_time(numero_matricula)                                                               