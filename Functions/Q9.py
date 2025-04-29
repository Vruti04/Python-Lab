#CP9

def count_alpha_digits(s):
    l=list(s)
    a=0
    n=0
    for i in l:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            n+=1
    return(a,n)

s=input("enter a string:")
a,n=count_alpha_digits(s)
d={'alpha':a,'number':n}
print(d)
