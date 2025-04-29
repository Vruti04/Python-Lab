#CP3

def create_array(x,y,z,v):
    l=[]
    for i in range(z):
        m=[]
        for j in range(y):
            n=[]
            for k in range(x):
                l=l+[v]
            m.append(n)
        l.append(m)
    return(l)
def input_():
    x=int(input("x="))
    y=int(input("y="))
    z=int(input("z="))
    v=int(input("value="))
    a=create_array(x,y,z,v)
    print(a)
input_()
