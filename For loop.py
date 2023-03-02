#for i in range(10): # 1, 2, 3, 4, 5, 6, 7, 8, 9
 #   print(i)
  #  print("$")


family = ["dad", 1.73, "mum", 1.68, "ema", 1.71, "bob", 1.60]
heights = [1.73, 1.68, 1.71, 1.60]

for height in heights:
    print(height * 2)

#enumerate
print(list(enumerate(heights)))

for index, height in enumerate(heights):
    print(index, height)


print("""
Strings
""")

characters = "Monty Python"
for char in characters:
    print(char +"!!!")

print("""
Arrays
""")

import numpy as np
heights_np = np.array(heights)
for height in heights_np:
    print(height * 100)

for i in characters.