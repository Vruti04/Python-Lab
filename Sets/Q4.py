#8.4
def set4():
    s = {'vidhi' , 'naiyya' , 'swaroopa' , 'vruti' , 'krissa'}
    sa = set()
    sb = set()
    for nm in s:
        if nm[0] == 'a':
            sa.add(nm)
        elif nm[0] == 'b':
            sb.add(nm)
    sa1 = {nm for nm in s if nm[0] == 'a'}
    print(sa)
    print(sb)#8.1
def set1():
    sentence = input("enter the sentence: ").split()
    print (sentence)
    s = set()
    s = {x.upper() for x in sentence}
    print(s)
set1()
