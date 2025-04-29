#CP11
import math
def sin_x(x, terms=10):
    result = 0
    for n in range(terms):
        # Taylor series term: (-1)^n * x^(2n+1) / (2n+1)!
        result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

x = float(input("Enter the value of x (in radians): "))

result = sin_x(x)
print(f"sin({x}) = {result}")
