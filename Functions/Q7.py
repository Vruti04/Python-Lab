#CP7

def ispalindrome(x):
    if x==x[::-1]:
        return (True)
    else:
        return(False)
x=input("enter the string:")
print(ispalindrome(x))
