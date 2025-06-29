"""

Atividade Prática 02
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""

#QUESTÃO 1

def converterMoeda():
  valor_reais = float(input())
  taxa_dolar = 5.20
  taxa_euro = 6.15
  valor_dolar = valor_reais / taxa_dolar
  valor_euro = valor_reais / taxa_euro

  print(f"O valor em Dólares é: ${round(valor_dolar, 2)}")
  print(f"O valor em Euros é: €{round(valor_euro, 2)}")

converterMoeda()

#QUESTÃO 2

def calcularDesconto():
  preco_original = 50.00
  porcentagem_desconto = 20

  valor_desconto = preco_original*(porcentagem_desconto/100)
  valor_final = preco_original - valor_desconto

  print("Nome do Produto: Camiseta")
  print("Preço unitário: R$ 50.00")
  print("Porcentagem de Desconto: 20%")
  print(f"Valor do Desconto: R$ {valor_desconto}")
  print(f"Preço final: R$ {valor_final}")

calcularDesconto()

#QUESTÃO 3

def calcularMedia():
  primeira_nota = 7.5
  segunda_nota = 8.0
  terceira_nota = 6.5

  media = (primeira_nota+segunda_nota+terceira_nota)/3

  print(f"Nota 1: {primeira_nota}")
  print(f"Nota 2: {segunda_nota}")
  print(f"Nota 3: {terceira_nota}")
  print(f"Média final: {round(media, 2)}")

calcularMedia()

#QUESTÃO 4

def calcularCombustivel():
  distancia_percorrida = 300
  combustivel_gasto = 25
  consumo_medio = distancia_percorrida/combustivel_gasto
  print(f"Distância percorrida: {distancia_percorrida} km")
  print(f"Quantidade de combustivel usada: {combustivel_gasto} litros")
  print(f"Consumo médio de combustível: {round(consumo_medio, 2)} km/l")

calcularCombustivel()

