heights = [1.73, 1.68, 1.71, 1.60] # colectie de date


# indexare  0      1     2      3     4      5     6       7
family = ["dad", 1.73, "mum", 1.68, "ema", 1.71, "bob", 1.60]

family2 = [
    ["dad", 1.73],
    ["mum", 1.68],
    ["ema", 1.71],
    ["bob", 1.60]
]

# adaugam elemente
# stergem elemente
# modificam elemente deja existente


# modificam elemente deja existente
family[-1] = 1,71
print(family)

family[0:2] = ["Dad", 1.75]
print(family)

# adaugam elemente
family = family + ["granny", 1.50]
print(family)

# stergem elemente
del(family[0])
print(family)



