#7.4

text = input("Enter a string: ")


char_freq = {}

for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequencies:", char_freq)

