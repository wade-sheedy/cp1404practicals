import random

How_Many_Numbers = int(input("How many numbers would you like? "))
Numbers_Generated = []
random.seed(a=None, version=2)
state = random.getstate()
for numbers in range(1, How_Many_Numbers + 1):
    random.setstate(state)
    Number_in_row = [].append(random.randint(0 ,46))
    Numbers_Generated.append(Number_in_row)
    print(Numbers_Generated)
