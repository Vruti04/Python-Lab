#q1
import random

odd_list = [random.randint(1,100)*2 -1 for _ in range(5)]
    print("list of 5 odd integers:", odd_list)
even_list = [random.randint(1,100)*2 for _ in range(4)]
    print("list of 4 even integers:", even_list)
odd_list[2] = even_list
    print("after replacing the third element:", odd_list)
flattened_list = []
    for item in odd_list:
        if isinstance(item,list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    print("flattened list:", flattened_list)
    flattened_list.sort()
        print("sorted flattened list:", flattened_list)
