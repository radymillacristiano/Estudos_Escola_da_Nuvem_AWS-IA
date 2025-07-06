"""
Exercicio 1: Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.

Exercicio 2: Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.

Exercicio 3: Crie uma função que verifique se uma palavra ou frase é um palindromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não".
"""

import string

#QUESTÃO 1

def calcula_gorjeta():
  try:
    totalConta = float(input("Digite o valor total da conta: R$ "))
    porcentagemGorjeta = float(input("Digite o valor da porcertagem da gorjeta: "))
    valorGorjeta = totalConta * (porcentagemGorjeta/100)
    print(f"O valor da gorjeta é R${round(valorGorjeta, 2)}")
  except ValueError:
    print("Entrada inválida. Use apenas números.")

calcula_gorjeta()

#QUESTÃO 2

def calcula_idade():
  anoNascimento = int(input("Digite o seu ano de nascimento: "))
  anoAtual = int(input("Digite o ano atual: "))
  diasIdade = (anoAtual-anoNascimento)*365
  print(f"A sua idade em dias é aproximadamente {diasIdade} dias.")

calcula_idade()

#QUESTÃO 3

def verifica_palindromo():
  frase = input("Digite uma palavra ou frase: ").lower()
  # Remove espaços, pontuação e acentos simples
  frase_limpa = ''.join(char for char in frase if char.isalnum())
  if frase_limpa == frase_limpa[::-1]:
    print("Sim")
  else:
    print("Não")

verifica_palindromo()