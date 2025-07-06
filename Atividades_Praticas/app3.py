"""
Exercicio 1: Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

Exercicio 2: Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.

Exercicio 3: Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

Exercicio 4: Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
Utilize a API da AwesomeAPI para obter os dados de cotação.​

"""

import random
import string
import requests

#QUESTÃO 1

def gerar_senha(tamanho):
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choices(caracteres, k=tamanho))
  return senha

tamanho = int(input("Digite a quantidade de caracteres para a senha: "))
print("Senha gerada:", gerar_senha(tamanho))

#QUESTÃO 2

url = "https://randomuser.me/api/"
resposta = requests.get(url)

if resposta.status_code == 200:
  dados = resposta.json()
  usuario = dados['results'][0]
  nome = f"{usuario['name']['first']} {usuario['name']['last']}"
  email = usuario['email']
  pais = usuario['location']['country']

  print("Nome:", nome)
  print("Email:", email)
  print("País:", pais)
else:
  print("Erro ao acessar a API.")

#QUESTÃO 3

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)

if resposta.status_code == 200:
  dados = resposta.json()
  if "erro" not in dados:
      print("Logradouro:", dados.get("logradouro", "N/A"))
      print("Bairro:", dados.get("bairro", "N/A"))
      print("Cidade:", dados.get("localidade", "N/A"))
      print("Estado:", dados.get("uf", "N/A"))
  else:
      print("CEP não encontrado.")
else:
  print("Erro ao acessar a API.")

#QUESTÃO 4

moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
  dados = resposta.json()
  chave = f"{moeda}BRL"
  if chave in dados:
      info = dados[chave]
      print("Moeda:", info['name'])
      print("Valor Atual:", info['bid'])
      print("Valor Máximo:", info['high'])
      print("Valor Mínimo:", info['low'])
      print("Última Atualização:", info['create_date'])
  else:
      print("Moeda não encontrada na resposta.")
else:
  print("Erro ao acessar a API.")
