"""
Fizzbuzz problem
-solved by Dewan
"""


def fizz_buzz(n):
    """
    Print numbers from 1 to n. For multiples of 3, print 'Fizz' instead of the number,
    for multiples of 5, print 'Buzz'. For numbers which are multiples of both 3 and 5, print 'FizzBuzz'.

    :param n: The upper limit of the range (inclusive).
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Example usage
fizz_buzz(15)
