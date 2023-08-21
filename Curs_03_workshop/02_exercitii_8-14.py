"""
8 - 9. Avand stringul 'Coral is either the stupidest animal or the smartest rock':
afiseaza de cate ori apare cuvantul 'the'
"""

text = "Coral is either the stupidest animal or the smartest rock"
cuvant_cautat = " the"
numarul_de_aparitii = text.lower().count(cuvant_cautat)
print("Cuvantul '{}' apare de {} ori in text. " .format(cuvant_cautat, numarul_de_aparitii))
print(f"Cuvantul '{cuvant_cautat}' apare de {numarul_de_aparitii} ori in text.")

print("-" * 40)

"""
10. Acelasi string:
    Foloseste un assert ca sa verifici daca acest string contine doar numere.
"""

assert text.isdigit() == False

print("-" * 40)

"""
11. Exercitiu: Citeste de la tastatura un string de dimensiune impara
    afiseaza caracterul din mijloc.
"""

input_string = input("Introdu un string de dimensiune impara: ")
if len(input_string) %2 != 0:
    mijlocul = len(input_string) // 2
    caracter_mijloc = input_string[mijlocul]
    print("Caracterul din mijloc este: ", caracter_mijloc)
else:
    print("Lungimea stringului nu este impara.")

print("-" * 40)

"""
12. Folosind o singura linie de cod:
    citeste un string de la tastatura (ex: alabala portocala);
    salveaza fiecare cuvant intr-o variabila
"""
cuvant1, cuvant2 = input("Introdu un string din doua cuvinte...").split()
print(cuvant1)
print(cuvant2)

print("-" * 40)

"""
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
"""


text = input('Introduceti un text ... ')
primul_caracter = text[0]
rezultat = ''
# print(text)
for caracter in text:
    if caracter == primul_caracter:
        rezultat += caracter.upper()
    else:
        rezultat += caracter
print(rezultat[0].lower()+rezultat[1:-1]+rezultat[-1].lower())


"""
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****

"""

user = input("Introdu un user: ")
parola = input("Introdu o parola: ")
lungime_parola = len(parola)
caractere_asterix = "*" * lungime_parola
print(f"Parola pentru user-ul {user} este {caractere_asterix} si are {lungime_parola} caractere")
