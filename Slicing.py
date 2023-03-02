#Slicing


heights = [1.73, 1.68, 1.71, 1.60] # colectie de date


# indexare  0      1     2      3     4      5     6       7
family = ["dad", 1.73, "mum", 1.68, "ema", 1.71, "bob", 1.60]

family2 = [
    ["dad", 1.73],
    ["mum", 1.68],
    ["ema", 1.71],
    ["bob", 1.60]
]

print(family[1:3])
#[start:stop] start este inclus iar stop nu este inclus



#print(family[8]) # daca accesam un index care nu exista primim eroare

print(family[7:9]) # daca accesam mai multi indecsi care nu exista atunci primim o lista goala
print(family[:4]) # daca omitem startul va afisa de la start
print(family[2:]) # la fel daca valoarea stop este omisa va include toate valoriel de la start pana la ultimul element (inclusiv)

# [start:stop:step]  step = increment (din cat in cat sa mearga)

numere = [0,1,2,3,4,5,6,7,8,9]

print(numere[::2]) #numere pare
print(numere[1::2]) #numere impare

print(numere[-4:-1])

