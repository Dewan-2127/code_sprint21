"""
Prime number checker problem
-solved by Dewan
"""


def is_checker(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number to check prime: "))

if is_checker(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

