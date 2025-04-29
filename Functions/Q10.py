#CP10

def freq(s):
    word=s.split()
    l={}
    for i in word:
        i=i.lower()
        if i in l:
            l[i]+=1
        else:
            l[i]=1
    f=sorted(l.items())
    return dict(f)
s=input("enter a string:")
r=freq(s)
print(r)
