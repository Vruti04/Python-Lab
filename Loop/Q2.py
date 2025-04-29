#CP2
def print_multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number to print its multiplication table: "))

print_multiplication_table(num)
