import pandas as pd

brics = pd.read_csv("brics.csv", index_col=0)

print(brics)

# a. metoda prin parantezele patrate
print("\n\n\n")
print(brics["capital"])

print(type(brics["capital"])) # o serie pandas este o matrice unidimensionala careia ii putem asocia o eticheta
print("\n\n\n")

print(brics[["capital"]])
print(type(brics[["capital"]]))

print(brics[["country", "capital"]])

print("\n\n\n selectarea randurilor")

print(brics[1:2])
print(brics[1:4])
print(brics[:])

# b. metode avansate care folosesc .loc si .iloc

# b.1 metode avansate care folosesc .loc (pe baza de eticheta)
print("\n\n\n")

print(brics.loc["IN"])
print(type(brics.loc["IN"]))

print(brics.loc[["IN", "SA"]])
print("\n\n\n")

print(brics.loc[["IN", "SA"], ["country", "capital"]])

print(brics.loc[:, ["country", "capital"]])
print("\n\n\n")



# b.1 metode avansate care folosesc .iloc (pe baza de index)

print(brics.iloc[[1]])
print(brics.iloc[[1,2,3]])




