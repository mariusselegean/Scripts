# DRY concept  - do not repeat yourself


height1 = 1.73
height2 = 1.68
height3 = 1.71
height4 = 1.60

heights = [1.73, 1.68, 1.71, 1.60] # colectie de date


# indexare  0      1     2      3     4      5     6       7
family = ["dad", 1.73, "mum", 1.68, "ema", 1.71, "bob", 1.60]

family2 = [
    ["dad", 1.73],
    ["mum", 1.68],
    ["ema", 1.71],
    ["bob", 1.60]
]
print(family2)
print(type(heights))
print(type(family))
print(type(family2))

print(heights + family) # se obtine o noua lista cu toate obiectele din ambele liste

print(family[1])
print(family[5])
print(family[-3])
print(family[-1])

print([1][1])

