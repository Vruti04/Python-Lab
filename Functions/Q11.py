#CP11

def create_list(l1,l2):
     inter = list(set(l1)&set(l2))
    return inter
l1=[1,2,3,4,5]
l2=[2,5,6,7,8]
r=create(l1,l2)
print(r)
     
