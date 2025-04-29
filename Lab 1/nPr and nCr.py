#Print nCr and nPr.
def fact(x):
    f=1
    for a in range(x,1,-1):
        f=f*a
    return f
n=int(input("Enter n:"))
r=int(input("Enter r:"))
nPr=fact(n)/fact(n-r)
nCr=nPr/fact(r)
print("nPr = ",nPr)
print("nCr = ",nCr)
