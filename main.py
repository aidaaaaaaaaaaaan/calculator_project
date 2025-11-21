from operations import add, subtract, multiply, divide
from utils import get_number

def main():
    print("Простой калькулятор с модулями")
    a = get_number("Введите первое число: ")
    b = get_number("Введите второе число: ")
    op = input("Выберите операцию (+, -, *, /): ")

    try:
        if op == "+":
            print("Результат:", add(a, b))
        elif op == "-":
            print("Результат:", subtract(a, b))
        elif op == "*":
            print("Результат:", multiply(a, b))
        elif op == "/":
            print("Результат:", divide(a, b))
        else:
            print("Неверная операция")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
