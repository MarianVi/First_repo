"""
    Bucla WHILE
- este iterator de control
- are nevoie de o conditie de start pentru a functiona (spre deosebire de for)
- daca nu are conditie de start, bucla nu porneste
- nu are nici start nici finish daca nu sunt definite explicit
- inainte de startul buclei WHILE, trebuie sa definim o variabila de initializare
- trebuie sa aiba si o conditie de terminare
- fara conditiile de initializare si de terminare vom avea o bucla infinita
"""

nr = 0               # initializare variabila

while nr < 10:               # conditia de rulare a buclei
    print(nr)
    nr += 1               # conditia de parcurgere (incrementare)

print('-' * 40)

# while True

x = 10
while True :
    print(x)
    x = x - 1
    if x == - 9:
        break

print('-' * 40)

# while merge si cu else
x = 10
while x > 2:
    print(x)
    x -= 1
else:
    print('Sfarsitul ciclului')