#CP4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

num = int(input("Enter a number: "))

print(f"\nChecking number: {num}")
print("Prime:", "Yes" if is_prime(num) else "No")
print("Perfect:", "Yes" if is_perfect(num) else "No")
print("Armstrong:", "Yes" if is_armstrong(num) else "No")
print("Palindrome:", "Yes" if is_palindrome(num) else "No")
print("Automorphic:", "Yes" if is_automorphic(num) else "No")

alpha_count, digit_count = count_alphabets_digits(user_input)

print("Number of alphabets:", alpha_count)
print("Number of digits:", digit_count)

