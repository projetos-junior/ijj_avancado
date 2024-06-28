import requests

cep = input("Por favor digite seu CEP:")

response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
print("Status code:", response.status_code)

data = response.json()
print("dados:", data['logradouro'])
