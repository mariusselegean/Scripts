import numpy as np

heights = [1.73, 1.68, 1.71, 1.89, 1.79]
weights = [65.4, 59.2, 63.6, 88.4, 38.7]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights / np_heights ** 2

print(bmi)
print(type(np_heights))

lista = [1 ,2 ,3]
np.array = np.array(lista)
print(lista+lista)
print(np.array + np.array)

print("accesarea elementelor dintr-un array   ")
print(bmi[1])
print(bmi[:3]) #primele 3

print(bmi > 23)
print(bmi[bmi > 23])
print(bmi[bmi > 21])