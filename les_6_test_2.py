import random

size = 1000000
start_random = 1
finish_random = 1000

array = [random.randint(start_random, finish_random) for _ in range(size)]

counter = dict()
frequency = 1
num = None

for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
    if counter[item] > frequency:
        frequency = counter[item]
        num = item

