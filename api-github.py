#Mini projeto consumindo a API do Github
#Como fazer requisições HTTP utilizando Python 

import requests

print('Github Users')
username = input('Qual é o nome do usuário? ')
#print(username)
url = f'https://api.github.com/users/{username}'
#Variável response vai receber requests.get
#Usaremos o método get pois iremos EXTRAIR recursos da API 
response = requests.get(url)
#Convertendo a informação para JSON
data = response.json()

#Usando o f string no Python é possível interpolar dados dentro de uma string
if response.status_code == 200:
    #print(data)
    print(f"Nome completo: {data['name']}")
    print(f"Bio: {data['bio']}")
    print(f"Localização: {data['location']}")
else: 
    print('Não foi possível encontrar o usuário')



