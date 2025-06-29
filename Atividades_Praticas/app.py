"""
1- Programa de Saudação
* Crie um programa que imprima a mensagem "Olá, mundo!" na tela.

2- Calculadora de Soma
* Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14. O programa deve calcular a soma e exibir o resultado.

3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.

4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""

#QUESTÃO 1

def main():
  print("Olá, mundo!")
main()

#QUESTÃO 2

def calcularSoma():
  numero1, numero2 = int(input()), int(input())
  print(numero1 + numero2)
calcularSoma()

#QUESTÃO 3

def calcularVolume():
  comprimento, largura, altura = 12, 14, 20
  volume = comprimento*largura*altura
  print(volume, "cm³")
calcularVolume()

#QUESTÃO 4

def calcularPreco():
  nome_produto = "Cadeira Infantil"
  preco_unitario = 12.40
  quantidade = 3

  preco_total = float(preco_unitario*3)

  print(f"Nome do Produto: {nome_produto}")
  print("Preço unitário: R$ 12.40")
  print("Quantidade: 3")
  print("Preço Total: R$", preco_total)

calcularPreco()