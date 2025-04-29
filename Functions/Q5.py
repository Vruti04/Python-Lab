#CP5
def pangram(s):
    a=set('abcdefghijklmnopqrstuvwxyz ')
    print(a)
    s=s.lower()
    s=set(s)
    return(a<=s)


s="a b c d e f ghijklmnopqrstuvwxyz"
print(pangram(s))
