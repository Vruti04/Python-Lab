# CP3
def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

print("Vowel count:", count_vowels("Functional Programming Rocks"))
