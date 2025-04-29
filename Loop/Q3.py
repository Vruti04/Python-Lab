#CP3
def count_alphabets_digits(text):
    alphabets = 0
    digits = 0
    for char in text:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    return alphabets, digits

user_input = input("Enter a string: ")

