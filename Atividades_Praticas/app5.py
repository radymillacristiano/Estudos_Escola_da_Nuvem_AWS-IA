"""
1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa

2 - Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

4 - Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.
"""

#QUESTÃO 1

def calcular():
    while True:
        try:
            primeiroNumero = float(input("Digite o primeiro número: "))
            segundoNumero = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada (+, -, *, /): ").strip()

            if operacao == '+':
                resultado = primeiroNumero + segundoNumero
            elif operacao == '-':
                resultado = primeiroNumero - segundoNumero
            elif operacao == '*':
                resultado = primeiroNumero * segundoNumero
            elif operacao == '/':
                if segundoNumero == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = primeiroNumero / segundoNumero
            else:
                print("Operação inválida. Tente novamente com +, -, * ou /.")
                continue

            print(f"Resultado: {resultado}")
            break

        except ValueError:
            print("Erro: você deve digitar apenas números.")
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

calcular()

#QUESTÃO 2

def classificar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print("Par")
                pares += 1
            else:
                print("Ímpar")
                impares += 1

        except ValueError:
            print("Erro: você deve digitar um número inteiro ou 'fim'.")

    print("\nResumo:")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

classificar_numeros()

#QUESTÃO 3

def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

        if senha.lower() == 'sair':
            print("Encerrado pelo usuário.")
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue

        if not any(char.isdigit() for char in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue

        print("Senha forte!")
        break

verificar_senha()

#QUESTÃO 4

def registrar_notas():
    notas = []

    while True:
        entrada = input("Digite uma nota de 0 a 10 (ou 'fim' para encerrar): ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um número entre 0 e 10.")
        except ValueError:
            print("Erro: você deve digitar um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {round(media, 2)}\n")
    else:
        print("Nenhuma nota válida foi inserida.")

registrar_notas()