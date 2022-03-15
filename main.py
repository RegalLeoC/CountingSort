from dtslib import *
import random

test = random.sample(range(1,20), 9)
# test = [9, 4, 1, 7, 9, 1, 2, 0]

print("******Original******")
print(f"{test}")

test = counting_sort(test)
print("******Counting Sort******")
print(f"{test}")
