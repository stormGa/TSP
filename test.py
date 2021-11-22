import copy
import random

num_city = 5
start = 1
path = list(range(1, num_city + 2))
path[num_city] = start
i = 0
j = 0
path_new = path.copy()
while i == j:
    i = random.randint(1, num_city-1)
    j = random.randint(1, num_city-1)
path_new[i], path_new[j] = path_new[j], path_new[i]
print('path:', path)
print('new path', path_new)
print(i)
print(j)
