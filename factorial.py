"""
Find factorial problem
-solved by Dewan
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    number = int(input("Enter a number to find the factorial: "))
    if number < 0:
        print("Factorial is not define for negative numbers")
    else:
        print(f"The factorial of Number {number} is : {factorial(number)}")
except ValueError:
    print("Please enter a valid number")


