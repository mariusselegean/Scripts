numar = int(input("Spune-mi un numar: "))
# sau se mai poate asa: numar = int(numar)
if numar % 2 == 0 and numar % 3 == 0:
    print("Numarul este divizibil cu 2 si cu 3")
elif numar % 2 == 0:
    print("Numarul este divizibil cu 3")
elif numar % 3 == 0:
    print("Numarul este divizibil cu 3")

else:
    print("Numarul nu este divizibil nici u 2 nici cu 3")
