
# Passo 1: Crie uma tupla com 5 frutas
tupla = ("maçã", "banana", "laranja", "uva", "melancia")
print("Frutas:", ', '.join(tupla))

# Passo 2: Altere a tupla para uma lista
lista = list(tupla)
print("Convertendo tupla em lista:", lista)

# Passo 3: Insira 2 frutas extras a essa lista
lista.extend(["abacaxi", "manga"])
print("Lista após adicionar frutas:", lista)

# Passo 4: Remova a primeira fruta da lista
del lista[0]
print("Lista após remover o primeiro elemento:", lista)

# Passo 5: Remova a última fruta da lista
del lista[5]
print("Lista após remover o último elemento:", lista)

# Passo 6: Faça um print com a primeira fruta da lista
print("Primeira fruta da lista:", lista[0])

# Passo 7: Faça um print com a quantidade de frutas da lista
print("Quantidade de frutas da lista:", len(lista))

# Passo 8: Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
dicionario = {
    "Nome": "João",
    "Idade": 30,
    "Profissão": "Engenheiro"
}

# Passo 9: Imprima somente o valor contido na chave Nome do dicionário
print("Nome no dicionário:", dicionario["Nome"])