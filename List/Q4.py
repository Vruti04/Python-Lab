#q4
import random
random_list = [random.randint(-50,50) for _ in range(30)]
print("generated list:", random_list)

positive_list = [num for num in random_list if num >0]
negative_list = [ num for num in random_list if num <0]
print("positive numbers:", positive_list)
print("negative numbers:", negative_list)
