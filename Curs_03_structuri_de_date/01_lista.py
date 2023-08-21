# Lista de elemente - list
"""
- o insiruire de elemente ordonate
- pot avea valori diferite
- este MUTABILA (mutable): inseamna ca se pot adauga, sterge sau inlocui elemente din lista
- putem accesa orice index
- putem pune valori repetabile
- se defineste cu: []
"""

lista_diversa = [2, 3.14, False, "Elefant", 12345]
print(f"lista_diversa : {lista_diversa}")

# Accesam elementul al 2-lea

element2 = lista_diversa[1]
print(f'element2 : {element2}')

# Accesam ultimul element

ultimul_element = lista_diversa[-1]
print(f'Ultimul element : {ultimul_element}')

# Verificam ce lungime are lista

lungime_lista = len(lista_diversa)
print(f'Lungimea listei este: {lungime_lista}')

# # Incercam sa accesam un element care depaseste lungimea listei
# un_element = lista_diversa[5]
# print(un_element)

print ("-" * 40)

# Operatii cu elemente din lista:
# Schimbarea / Inlocuirea unui element din lista

lista_diversa[2] = True
print(f'Lista diversa : {lista_diversa}')

print ("-" * 40)
# Adaugarea unui nou element intr-o lista
# La final se face cu append
lista_diversa.append('asta la vista')
print(f'Lista diversa : {lista_diversa}')

# In interiorul listei cu insert
lista_diversa.insert(3, 10*10)
print(f'Lista diversa : {lista_diversa}')

print ("-" * 40)

# Stergerea unui element din lista :
lista_diversa.pop()
print(f'Lista diversa : {lista_diversa}')
# Pe baza de index
lista_diversa.pop(2)
print(f'Lista diversa : {lista_diversa}')

# List Slicing
# inversarea listei:
lista_inversa = lista_diversa[::-1]
print(f'Lista inversa : {lista_inversa}')

# parte din lista (ultimele 3 elemente din lista) :
print(f'Lista inversa, ultimele 3 elemente : {lista_inversa[-3:]}')