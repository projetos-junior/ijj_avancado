import pandas as pd

# # Carregando o arquivo CSV
dados = pd.read_csv('./aula8/dados_ficticios.csv')

df = pd.DataFrame(data=dados)
print(dados)
# # Filtrando os dados conforme os critérios fornecidos
# # 1. Pessoas com idade maior que 40 anos
filtro_idade_maior_40 = df[df['idade'] > 40]

# # # 2. Pessoas com renda maior que 5 mil
filtro_renda_maior_5000 = df[df['renda'] > 5000]

# # # 3. Pessoas com renda maior que 15 milcls
filtro_renda_maior_15000 = df[df['renda'] > 15000]

# # Exibindo os resultados
print("Pessoas com idade maior que 40 anos:\n", filtro_idade_maior_40)
print("\nPessoas com renda maior que 5 mil:\n", filtro_renda_maior_5000)
print("\nPessoas com renda maior que 15 mil:\n", filtro_renda_maior_15000)


