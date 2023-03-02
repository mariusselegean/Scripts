"""Cerinta: Scrieti un program care sa primeasca un numar natural n si sa afiseze toate numerele
naturale de la 1 la n.
Rezultate asteptate:
• Pentru n = 5, programul trebuie sa afiseze 1 2 3 4 """


n = int(input("xxx"))
i = 1
while i <= n:
    print(i)
    i += 1


"""Cerinta: Scrieti un program care sa determine suma cifrelor unui numar natural.
Rezultate asteptate:
• Pentru numarul 123, programul trebuie sa returneze 6.
• Pentru numarul 999, programul trebuie sa returneze 27."""

numar = input("Introduceți un număr natural: ")
suma_cifre = 0

for cifra in numar:
    suma_cifre += int(cifra)

print("Suma cifrelor numărului", numar, "este:", suma_cifre)