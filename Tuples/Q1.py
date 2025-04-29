#Q1
names_list=[("b1",),("b2",),"g1","g2","g3",("b3",),"g4",("b4",)]
boy_count=sum(1 for name in names_list if isinstance(name,tuple))
girl_count=sum(1 for name in names_list if isinstance(name,str))

print("Number of boys:",{boy_count})
print("Number of girls:",{girl_count})
    
