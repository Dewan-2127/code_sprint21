"""
Basic calculator Problem
-solved by Dewan
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not possible"
    return a / b


def main():
    choice = input("Enter 1 for Add, 2 for Subtract, 3 for Multiply, and 4 for Divide: ")
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input.")
        return

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(number1, number2))
    elif choice == '2':
        print("Result: ", subtract(number1, number2))
    if choice == '3':
        print("Result: ", multiply(number1, number2))
    elif choice == '4':
        print("Result: ", divide(number1, number2))


if __name__ == "__main__":
    main()
