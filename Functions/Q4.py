#CP4

def sum_(a,b,c,d,e):
     f=a+b+c+d+e
     return(f)
def avg_(a,b,c,d,e):
     f=(a+b+c+c+d+e)//5
     return(f)
def input1():
     a=int(input("enter 1st numbers:"))
     b=int(input("enter 2nd numbers:"))
     c=int(input("enter 3rd numbers:"))
     d=int(input("enter 4th numbers:"))
     e=int(input("enter 5th numbers:"))
     g=sum_(a,b,c,d,e)
     h=avg_(a,b,c,d,e)
     print("the sum of 5 numbers:",g)
     print("the avg of 5 number:",h)
input1()
 
