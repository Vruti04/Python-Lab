#CP8

def convert(s1):
    s=set(s1)
    l=str(s)
    print(l)
    s1="".join(sorted(s))
    return s1
s1=input("enter a string:")
print(convert(s1))
