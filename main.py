import os
import time

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


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')

