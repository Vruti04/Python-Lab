#q2
        
import random
random_list = [random.randint(1,10) for _ in range(20)]
print("generated list:",random_list)
num = int(input("enter a number to find its positions:"))
    positions = []
        for i in range(len(random_list)):
            if random_list [i] == num:
            positions.append(i)
    print(f"positions of {num} in the list:{positions}")
