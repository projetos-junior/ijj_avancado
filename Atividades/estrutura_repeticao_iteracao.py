'''
Estruturas de Repetição e Iteração
O que são estruturas de repetição e iteração?
Estruturas de repetição e iteração são construções de programação que permitem a execução repetida de um bloco de código enquanto uma condição específica é verdadeira. Elas são fundamentais para automatizar tarefas repetitivas e para a criação de algoritmos eficientes.

Quando são usadas?
Essas estruturas são usadas em diversas situações, como:

Processamento de listas ou outros tipos de coleções.
Execução de tarefas até que uma condição seja satisfeita.
Repetição de operações em intervalos regulares.
Implementação de algoritmos que exigem múltiplas passagens sobre um conjunto de dados.
Principais tipos de estruturas de repetição
Os principais tipos de estruturas de repetição em Python são: for, while, e compreensão de listas (list comprehensions).
'''
#Exemplo:
#For Loop: O for loop itera sobre uma sequência (como uma lista, tupla, dicionário, conjunto, ou string) e executa um bloco de código para cada item da sequência.

frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)


#Exemplo:
#While Loop: O while loop continua executando o bloco de código enquanto uma condição especificada é verdadeira.

contador = 0
while contador < 5:
    print(contador)
    contador += 1

#Exemplo:
'''
Compreensão de Listas (List Comprehensions):
As compreensões de listas oferecem uma maneira concisa de criar listas. 
Elas são usadas para aplicar uma expressão a cada item em uma sequência, 
filtrando opcionalmente itens que não satisfazem uma condição.
'''
quadrados = [x**2 for x in range(10)]
print(quadrados)


#Exemplo:
#Processamento de Dados: Suponha que temos uma lista de vendas diárias e queremos calcular a soma total das vendas.
vendas = [250, 300, 150, 400, 100]
total_vendas = 0
for venda in vendas:
    total_vendas += venda
print(total_vendas)


#Exemplo:
#Validação de Entrada: Continuar pedindo ao usuário uma entrada válida até que ele forneça uma.
while True:
    entrada = input("Digite um número positivo: ")
    if entrada.isdigit() and int(entrada) > 0:
        print(f"Você digitou um número válido: {entrada}")
        break
    else:
        print("Entrada inválida, tente novamente.")


#Exemplo:
#Filtros e Transformações: Suponha que temos uma lista de números e queremos criar uma nova lista apenas com os números pares, elevados ao quadrado.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_quadrados = [num**2 for num in numeros if num % 2 == 0]
print(pares_quadrados)

#Esses exemplos demonstram como as estruturas de repetição e iteração são utilizadas para automatizar tarefas comuns e manipular dados de maneira eficiente.
