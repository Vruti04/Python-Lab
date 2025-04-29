#Area is greater then perimeter of rectangle
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
#Area of rectangle
Area=l*b
print("The area of Reactangle is:",Area)
#Perimeter of rectangle
Peri=2*(l+b)
print("The perimeter of rectangle is:",Peri)
#Greater than
if Area>Peri:
    print("Areais greater than its perimeter")
else:
    print("Perimeter is greater than Area")
