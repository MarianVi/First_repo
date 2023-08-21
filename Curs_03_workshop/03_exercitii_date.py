"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

Raspuns: Este o structura care controleaza si permite o executare diferita a codului in functie de evaluarea
unei conditii.
"""

"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""
x = int(input("Introdu un numar: "))
if x >= 1:
    print(f"{x} este un numar natural")
else:
    print(f"{x} nu este un numar natural")


print("-" * 40)
"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
if x > 0:
    print(f"{x} este un numar pozitiv")
elif x < 0:
    print(f"{x} este un numar negativ")
else:
    print(f"{x} este un numar neutru")


print("-" * 40)
"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
if x > -2 and x < 13:
# if -2 < x < 13:
    print(f"{x} este cuprins in intervalul - 2 si 13")
else:
    print(f"{x} nu este cuprins in intervalul -2 si 13")


print("-" * 40)
"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
y = int(input("Introdu al doilea numar: "))
z = x - y
if z < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica decat 5")
else:
    print(f"Diferenta dintre {x} si {y} nu este mai mica decat 5")


print("-" * 40)
"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
if not 5 <= x <= 27:
    print(f"{x} nu este intre 5 si 27")
else:
    print(f"{x} este intre 5 si 27")


print("-" * 40)
"""
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
if x > y:
    print(f"{x} este mai mare decat {y}")
elif x < y:
    print(f"{y} este mai mare decat {x}")
else:
    print("Numerele sunt egale")


print("-" * 40)
"""
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""

a = int(input("Introdu un numar: "))
b = int(input("Introdu al doilea numar: "))
c = int(input("Introdu al treilea numar: "))

if a == b == c:
    print("Este un triunghi echilateral")
elif a == b and a != c:
    print("Este un triunghi isoscel")
elif a != b and b == c:
    print("Este un triunghi isoscel")
else:
    print("Este un triunghi oarecare")

print("-" * 40)
"""
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
"""
litera = input("Tasteaza o litera: ").lower()
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print(f'{litera} este o vocala')
else:
    print(f'{litera} nu este o vocala')

print("-" * 40)
"""
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

nota = float(input("Scrie nota primita: "))

if nota >= 9:
    nota = 'A'
    print(f'Nota ta este: {nota}')
elif nota >= 8:
    nota = 'B'
    print(f'Nota ta este: {nota}')
elif nota >= 7:
    nota = 'C'
    print(f'Nota ta este: {nota}')
elif nota >= 6:
    nota = 'D'
    print(f'Nota ta este: {nota}')
elif nota > 4:
    nota = 'E'
    print(f'Nota ta este: {nota}')
else:
    nota = 'F'
    print(f'Nota ta este: {nota}')

print("-" * 40)
"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
x = int(input('Adauga un numar din 4 cifre: '))
count = 0
while (x>0):
    count = count + 1
    x = x // 10
if count >= 4:
    print(f"Numarul are {count} cifre")
else:
    print('Numarul nu are minimul de 4 cifre')

print("-" * 40)
"""
12.Verifică dacă x are exact 6 cifre.
"""

x = int(input('Introdu un numar din 6 cifre: '))
count = 0
while (x>0):
    count = count + 1
    x = x // 10
if count == 6:
    print(f"Numarul are exact {count} cifre")
else:
    print('Numarul nu are 6 cifre')

print("-" * 40)
"""
13.Verifică dacă x este număr par sau impar (x e int).
"""

x = int(input('Introduceti un numar: '))
if x % 2 == 0:
    print(f'{x} este un numar par')
else:
    print(f'{x} este un numar impar')


print("-" * 40)
"""
14. x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""

x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))

if x >= y and x >= z:
    print(f'{x} este cel mai mare numar dintre cele 3')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar dintre cele 3')
elif z >= y  and z >= x:
    print(f'{z} este cel mai mare numar dintre cele 3')
else:
    print('Numerele sunt egale')

print("-" * 40)

"""
15. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""

text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti un numar: '))
print(text[:-x])

print("-" * 40)
"""
16. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""

text = 'Coral is either the stupidest animal or the smartest rock'
print(text[:5] + text[-5:])

print("-" * 40)
"""
17. Același string.
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest'
"""

text = 'Coral is either the stupidest animal or the smartest rock'
index = text.index('ro')
print(index)
text = text[:53]
print(text)

print("-" * 40)
"""
18. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""

import random

dice_roll = random.randint(1, 100)
print(dice_roll)
guess = int(input('Ghiceste numarul: '))
if guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess}, dar a fost {dice_roll}')
elif guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess}, dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Ai ales {guess} si zarul a fost {dice_roll}. Felicitari!')

print("-" * 40)

