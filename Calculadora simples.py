import math

def calculator():
    print("Bem-vindo à calculadora!")
    print("Digite 1 para soma")
    print("Digite 2 para subtração")
    print("Digite 3 para multiplicação")
    print("Digite 4 para divisão")
    print("Digite 5 para exponenciação")
    print("Digite 6 para raiz quadrada")
    print("Digite 7 para sair")

    choice = int(input("Digite sua escolha (1/2/3/4/5/6/7): "))

    if choice == 1:
        num1, num2 = get_input()
        result = num1 + num2
        print_result(result)
    elif choice == 2:
        num1, num2 = get_input()
        result = num1 - num2
        print_result(result)
    elif choice == 3:
        num1, num2 = get_input()
        result = num1 * num2
        print_result(result)
    elif choice == 4:
        num1, num2 = get_input()
        result = num1 / num2
        print_result(result)
    elif choice == 5:
        num1, num2 = get_input()
        result = pow(num1, num2)
        print_result(result)
    elif choice == 6:
        num1 = float(input("Digite o número: "))
        result = math.sqrt(num1)
        print_result(result)
    elif choice == 7:
        exit()
    else:
        print("Opção inválida. Tente novamente.")

def get_input():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def print_result(result):
    print("Resultado: ", result)

if __name__ == '__main__':
    calculator()
