#CP6

def tuple_in_list(x):
    l=[]
    k=()
    for i in range(1,x+1):
        k=(i,i*i,i*i*i)
        l.append(k)
    return l
x=int(input("enter a number:"))
print(tuple_in_list(x))
