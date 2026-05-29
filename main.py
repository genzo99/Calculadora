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
            print("\nOperações disponíveis:")
            print("+  Soma")
            print("-  Subtração")
            print("*  Multiplicação")
            print("/  Divisão")
            print("** Exponenciação")
            print("%  Módulo\n")

            operador = input("Escolha a operação: ")

            resultado1 = calculadora(num1, num2, operador)
            resultado2 = calculadora_alt(num1, num2, operador)

            print(f"\nResultado (função 1): {resultado1}")
            print(f"Resultado (função 2): {resultado2}")

            if str(resultado1) == "nan" or str(resultado2) == "nan":
                print("\nOperação inválida!")
        


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')

