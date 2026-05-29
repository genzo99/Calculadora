import os
import time
import math

def calculadora(num1: float, num2: float, operador: str) -> float:
    
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        result = num1 % num2

    return result


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            print('Calculadora')
            print('----------------------------------\n')

            num1 = float(input("Introduza o primeiro número: "))
            num2 = float(input("Introduza o segundo número: "))

            print("\nOperações disponíveis:")
            print("+  Soma")
            print("-  Subtração")
            print("*  Multiplicação")
            print("/  Divisão")
            print("** Exponenciação")
            print("%  Módulo\n")

            operador = input("Escolha a operação: ")

            resultado = calculadora(num1, num2, operador)

            print(f"\nResultado: {resultado}")

            if math.isnan(resultado):
                print("\nOperação inválida!")

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)
            continue

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            continue

        repetir = input("\nDeseja continuar? (s/n): ").lower()
        if repetir not in ("s", "sim"):
            break

    print('\nVolte sempre!\n')

