
"""
Creati un program care are ca scop un meniu.
Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5
captat intr-o variabila.
Prezentati prin afisare acest sir de caractere:
“””
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Q - Iesire din program
“””

Apoi folosindu-va de o constructie if-elif-else afisati:
- daca utilizatorul scrie de la tastaura 1 afisati “Afisare lista de cumparaturi”
- daca utilizatorul scrie de la tastaura 2 afisati “Adugare element”
- daca utilizatorul scrie de la tastaura 3 afisati “Stergere element”
- daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturi”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element”
- daca utilizatorul scrie altceva de la tastaura afisati “Alegerea nu exista.
Reincercati”
- daca utilizatorul scrie de la tastaura Q afisati “Iesire din program”

"""

#lista cumparaturi
lista = ["apa", "lapte"]


while True:
    optiune = input("""
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Q - Iesire din program
    """)
    if optiune == "1":
        print("Afisare lista de cumparaturi")
        print(lista)

    elif optiune == "2":
        element = input("Adauga un element: ")
        lista.append(element)
        print("Adugare element")
        print(lista)

    elif optiune == "3":
        print("Stergere element")
        element = input("Sterge un element: ")
        if element in lista:
            lista.remove(element)
            print("Elementul a fost sters")
        else:
            print("Elementul nu a fost identificat in lista!")
        print(lista)

    elif optiune == "4":
        print("Sterere lista de cumparaturi")
        lista.clear()
        print("Lista a fost stearsa!!!")

    elif optiune == "5":
        print("Cautare in lista de cumparaturi")
        element = input("Cauta un element din lista: ")
        if element in lista:
            print("Elementul se afla in lista!")
        else:
            print("Elementul nu se afla in lista!")

    elif optiune =="6":
        print("Iesire din program")
    elif optiune.upper() == "Q":
        print("Quit")
        break
    else:
        print("Iesire din program. Reincercati! ")
