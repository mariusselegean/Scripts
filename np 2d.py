import numpy as np

heights = [1.73, 1.68, 1.71, 1.89, 1.79]
weights = [65.4, 59.2, 63.6, 88.4, 38.7]

list_2d = [
    heights,
    weights
]

np_2d = np.array(list_2d)
print(np_2d)
print(type(np_2d))

print(np_2d.shape) # 2,5 inseamna nr de randuri 2 si numar coloane 5
print(np_2d[1][2])
print(np_2d[1, 2])
#print(np_2d[1, 2:4]) #slicing
#print(np_2d[:, 1:3])

