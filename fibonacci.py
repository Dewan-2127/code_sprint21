def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


print(fibonacci_series(10))

