def lower(s):
    result=""
    for char in s:
        if 'A' <=char<='Z':
            result += chr(ord(char)+32)
        else:
            result+=char
    return result
    
def upper(s):
    result=""
    for char in s:
        if 'a' <=char<='z':
            result += chr(ord(char)-32)
        else:
            result+=char
    return result
def toggle(s):
    result=""
    for char in s:
        if 'a' <=char<='z':
            result += chr(ord(char)-32)
        elif 'A' <=char<='Z':
            result += chr(ord(char)+32)
        else:
            result+=char
    return result
s=input("Enter a string: ")
    
print("original word",s)
print("Lowercase word",lower(s))
print("Upper word",upper(s))
print("Toggle word",toggle(s))
