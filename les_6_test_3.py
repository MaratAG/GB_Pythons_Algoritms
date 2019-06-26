import random
from collections import Counter

size = 1000000
start_random = 1
finish_random = 1000

array = [random.randint(start_random, finish_random) for _ in range(size)]

frequency = list(dict(Counter(array)).items())
frequency.sort(key=lambda i: i[1], reverse=True)
