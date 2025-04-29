#CP9
def print_reverse_natural_numbers(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

num = int(input("Enter N: "))

print_reverse_natural_numbers(num)
