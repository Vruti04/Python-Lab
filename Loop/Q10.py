#CP10
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_sequence = fibonacci(num)
print(f"First {num} Fibonacci numbers: {fib_sequence}")
