#8.1
def set1():
    sentence = input("enter the sentence: ").split()
    print (sentence)
    s = set()
    s = {x.upper() for x in sentence}
    print(s)
set1()
