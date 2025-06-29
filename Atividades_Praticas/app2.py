"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).

2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"

3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

"""

#QUESTÃO 1

def classificarIdade():
  idade = int(input("Digite a idade: "))
  
  if idade >= 0 and idade <= 12: {
    print("O usuário é criança")
  } 
  elif idade >= 13 and idade <= 17: {
    print("O usuário é adolescente")
  }
  elif idade >= 18 and idade <= 59: {
    print("O usuário é adulto")
  }
  elif idade >= 60: {
    print("O usuário é idoso")  
  }

classificarIdade()

#QUESTÃO 2

def calcularIMC():
  peso = int(input("Por favor, digite o seu peso em kilogramas: "))
  altura = float(input("Por favor, digite a sua altura em metros: "))

  imc = peso/(altura**2)

  if imc < 18.5:
    print(f"O seu IMC é {round(imc, 2)}. Você está abaixo do peso.")
  elif imc >= 18.5 and imc <= 24.9:
    print(f"O seu IMC é {round(imc, 2)}. Você está com peso normal.")
  elif imc >= 25 and imc <= 29.9:
    print(f"O seu IMC é {round(imc, 2)}. Você está com sobreso.")
  else:
    print(f"O seu IMC é {round(imc, 2)}. Você está obeso.")

calcularIMC()

#QUESTÃO 3

def converterTemperatura():
  temperatura = int(input("Digite a temperatura: "))
  unidade_original = input("Informe a unidade de medida de origem da temperatura (Digite C para Celsius, F para Fahrenheit e K para Kelvin): ").upper()
  unidade_conversao = input("Informe a unidade de medida que você deseja obter a temperatura (Digite C para Celsius, F para Fahrenheit e K para Kelvin): ").upper()

  if unidade_original == "C" and unidade_conversao == "F":
      resultado = (temperatura * 9/5) + 32
      print(f"Resultado: {resultado} Fahrenheit.")
      
  elif unidade_original == "C" and unidade_conversao == "K":
      resultado = temperatura + 273.15
      print(f"Resultado: {resultado} Kelvin.")
      
  elif unidade_original == "F" and unidade_conversao == "C":
      resultado = (temperatura - 32) * 5/9
      print(f"Resultado: {resultado} Celsius.")
      
  elif unidade_original == "F" and unidade_conversao == "K":
      resultado = ((temperatura - 32) * 5/9) + 273.15
      print(f"Resultado: {resultado} Kelvin.")
      
  elif unidade_original == "K" and unidade_conversao == "C":
      resultado = temperatura - 273.15
      print(f"Resultado: {resultado} Celsius.")
      
  elif unidade_original == "K" and unidade_conversao == "F":
      resultado = ((temperatura - 273.15) * 9/5) + 32
      print(f"Resultado: {resultado} Fahrenheit.")
      
  else:
      print("Unidade inválida. Use apenas C, F ou K.")

converterTemperatura()

#QUESTÃO 4

def classificarAno():
  ano = int(input("Digite o ano: "))

  if ano%4 == 0:
    if ano%100 == 0:
      if ano%400 == 0:
        print(f"O ano {ano} é bissexto.")
      else:
        print(f"O ano {ano} não é bissexto.")
    else:
        print(f"O ano {ano} é bissexto.")
  else:
    print(f"O ano {ano} não é bissexto.")

classificarAno()