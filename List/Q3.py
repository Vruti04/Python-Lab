#q3
import random
random_list = [random.randint(1,30) for _ in range (50)]
print("original list:", random_list)
i = 0
while i < len(random_list):
    if random_list.count(random_list[i]) >1:
        random_list.pop(i)
    else:
        i+=1
print("list after removing duplicates:", random_list)
