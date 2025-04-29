#CP7
import math
def nCr(n, r):
    return math.comb(n, r)  

def nPr(n, r):
    return math.perm(n, r)  

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"\n{n}C{r} = {nCr(n, r)}")
print(f"{n}P{r} = {nPr(n, r)}")
