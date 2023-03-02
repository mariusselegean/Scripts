numar = 5 # variabila cu eticheta numar si informatia stocata 5
par = 2
impar = 7

print(numar)
print(par)
print(impar)

#reguli pentru numele variabilelor
# 1. numele variabilelor nu pot contine spatii
# 2. nu poate incpe cu numere sau alte caractere speciale, doar cu litere
# 3. nu putem folosi keywords. (ex: for, while, break....)
# 4. numele unei variabile nu poate confine doar litere si cifre si underscore.
# 5. CAMELCASE - aceastaEsteOVariabila
# 6. SNAKECASE - aceasta_este_o_variabila

###########################################
# Tipuri de variabile / Tipuri de date
###########################################

# toate tipurile de date sunt clase, o clasa este un template sau blueprint.
# variabilele sunt obiecte
# ex: planul de arhitectura este clasa iar obiectul este casa
# Despre un obiect putem sa spunem ce stim despre obiect si ce stie sa faca obiectul
#

# Numere - sunt de 3 feluri

# integer, float, numere complexe.

var_int = -2 # numere intreci cu plus sau cu minus
var_float = 5.3  # numerele cu virgula cu plis si minus
var_complex = 2 + 3j  # partea reala plus partea imaginara.

print(type(var_int)) # afla tipul variabilei
print(type(var_float))
print(type(var_complex))

# Siruri Python (Stringuri) STR
string = 'orice text'
string2 = "orice text"

# BOOLEAN (True si False)
boolean = True # 1
boolean = False # 0

# liste in python  - secventa ordonata de valori si pot fi modificate dupa ce au fost create.

var_lista = [2, 5, 7, -44, 4+5j]
var_lista_goala = []
print(type(var_lista))

# TUPLE - secventa ordonata de valori si nu pot fi modificate dupa ce au fost create.

var_tuple = (4, 5, 6, -4, [2, 5, 7, -44, 4+5j])
print(type(var_tuple))

# SETURI - secvente neordonate de valori UNICE

var_set = {1, 2, 3, 4, 7, 9, 18}
print(type(var_set))

# DICTIONAR - secvente neordonate cu cheie si valoare (nume este cheia si python este valoarea)
dictionar = {"nume": "python", "prenume": "MONTY"}
print(type(dictionar))
