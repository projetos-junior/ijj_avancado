import pandas as pd

# Criando a lista de dados
dados = {
    'Nome': ['Carlos', 'Ana', 'João', 'Maria', 'Pedro', 'Beatriz', 'Lucas'],
    'Idade': [25, 30, 22, 35, 28, 27, 40],
    'Cidade': ['Recife', 'Recife', 'Recife','Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

# Criando o DataFrame
df = pd.DataFrame(data=dados)

# Filtrando os moradores de Recife
moradores_recife = df[df['Cidade'] == 'Recife']

# Exibindo o resultado
print(moradores_recife)