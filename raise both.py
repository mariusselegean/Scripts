def raise_both(param1, param2):
    result1 = param1 ** param2
    result2 = param2 ** param1
    return (result1, result2)

var1, var2 = raise_both(2, 3)
print(var1)
print(var2
      )
# tuple example: (nume, prenume, varsta, hobby) = ("Monty", "Python", 34, "serial")
nume, prenume, varsta, hobby= "Monty", "Python", 34, "serial"

print("*****")
print(nume)
print(prenume)
print(varsta)
print(hobby)



import pandas as pd

df = pd.read_csv("tweets.csv")
print(df)