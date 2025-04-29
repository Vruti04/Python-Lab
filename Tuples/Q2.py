#Q2
students=[(101,"Vidhi",19),\
          (103,"Swaroopa",20),\
          (102,"Naiyya",26),\
          (104,"Dharm",27),\
          (105,"Haard",21)]
roll_number=[]
names=[]
ages=[]

for student in students:
    roll_number.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll number of the student:",roll_number)
print("Name of the student :",names)
print("age of the student :",ages)
