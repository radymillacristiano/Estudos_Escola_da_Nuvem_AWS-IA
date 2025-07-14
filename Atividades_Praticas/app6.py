"""
1 - Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.

2 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.

3 -  Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos:
- Nome, Idade e Cidade.
"""

#QUESTAO 1
import csv
import json

pessoas = [
    {"Nome": "Maria", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Pedro", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Aline", "Idade": 22, "Cidade": "Belo Horizonte"}
]

with open('pessoas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor.writeheader()
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print("Arquivo pessoas.csv criado com sucesso!")

#QUESTAO 2

with open('pessoas.csv', mode='r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")

#QUESTAO 3

pessoa = {
    "Nome": "João",
    "Idade": 28,
    "Cidade": "Fortaleza"
}

with open('pessoa.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

print("Arquivo pessoa.json criado com sucesso!")

with open('pessoa.json', 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(f"Nome: {dados['Nome']}, Idade: {dados['Idade']}, Cidade: {dados['Cidade']}")
