# dictionary

pop = [30.55, 2.77, 39.21]

countries = ["Afganistan", "Albania", "Algeria"]

#care este populatia albaniei?

idx = countries.index("Albania")

print(idx, "index")
print(pop[idx], "populatia Albaniei")

info = {"Afganistan": 30.55, "Albania": 2.77, "Algeria": 39.21}
print(info["Albania"], "Populatia albaniei din dict")
# nume dict = {cheie: valoare}
#cheia unui dictionar trebuie sa fie unica

print(info)

info["sealand"] = 0.0028
print(info, "noul dictionar")

info.update(
    {"str":2, "str2": 3}
)

print(info , "noul dict")

#stergere elemente
del(info["str"])
print(info)

info["sealand"] = 0.0029
print(info)