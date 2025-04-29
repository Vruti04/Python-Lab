#Q6
def modifiy_element_of_tuple():
    t1=('A','B','C','D')
    t1_list=list(t1)
    t1_list[2]='V'
    t2=tuple(t1_list)
    print(t2)
modifiy_element_of_tuple()
