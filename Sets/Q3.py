#8.3
def set3():
    s = set()
    for i in range(5):
        s.add(input("Enter a name: "))
    print(s)
    nm = input("enter a name to modify: ")
    if nm in s:
        newnm = input("replace it with: ")
        s.pop(nm)
        s.add(newnm)
    else:
        print(nm,"not found")
    print(s.popitem(), " is deleted ")
    print(s.popitem(), " is deleted ")
    print("The final list: ", s)
    
set3()

