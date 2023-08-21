"""1. In cadrul unui comentariu, explica cu cuvintele tale ce este o variabila:
In limbajul de programare Python, o variabila reprezinta o locatie de memorie, unde se pot stoca date.
Aceasta actioneaza ca un container pentru a pastra informatii temporare sau permanente, cum ar fi numere, texte, liste,
obiecte sau alte tipuri de date"""

print("-" * 40)

"""2. Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de variabila:
string
int
float
bool"""

# String
nume = "Maria"
# Int
varsta = 17
# Float
inaltime = 1.79
# Boolean
este_minora = True

print("-" * 40)

"""
3. Utilizeaza functia type pentru a verifica daca au tipul de date asteptat
"""
# String
nume = "Maria"
print(type(nume))
# Int
varsta = 17
print(type(varsta))
# Float
inaltime = 1.79
print(type(inaltime))
# Boolean
este_minora = True
print(type(este_minora))

print("-" * 40)


"""
4. Rotunjeste 'float-ul' folosind functia round() si salveaza aceasta modificare in aceeasi variabila
(suprascriere): Verifica tipul acesteia
"""

#Variabila de tip float
inaltime = 1.79
print("Tipul variabilei 'inaltime' este, ", type(inaltime))
inaltime = round(inaltime)
print("Tipul variabilei 'inaltime' este, ", type(inaltime))

print("-" * 40)

"""
5. Foloseste print() si printeaza in consola 4 propozitii folosind cele 4 variabile. Rezolva nepotrivirile de tip prin 
ce modalitate doresti
"""
print(nume + " este colega mea")
print("Ea are " + str(varsta) + " ani")
print("Si are " + str(inaltime) + " metri inaltime")
print("Si este " + str(este_minora) + " ca sunt minora")

print("-" * 40)

"""
6. Citeste de la tastatura: 
numele
prenumele
Afiseaza: ' Numele complet are x caractere'
"""
# nume = input("Introdu numele...")
# prenume = input("Introdu prenumele...")
# nume_complet = nume + " " + prenume
# print("Numele complet are " + str(len(nume_complet)) + " caractere")

print("-" * 40)

"""
7. Citeste de la tastatura:
lungimea
latimea
Afiseaza: 'Aria dreptunghiului este x'.
"""

lungime = int(input("Introdu lungimea dreptunghiului..."))
latimea = float(input("Introdu latimea dreptunghiului..."))

aria = lungime * latimea

print("Aria dreptunghiului este ", aria)
