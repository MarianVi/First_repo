# SET -
"""
- este o colectie de elemente UNICE (nu poate avea valori duplicate)
- nu este ordonat
- este MUTABLE (doar adaugam si stergem, dar nu putem modifica elemente)
- fiecare element din SET trebuie sa fie IMUTABLE
- pot fi diverse tipuri de variabile
- valorile setului fiind unice sunt considerate ca si keys
- un set gol se defineste: set()
"""

# Facem un set
data_curenta = {2023, 'iulie', 11, True, 19, 49, 'PM'}
print(f'Data curenta : {data_curenta}')

print("-" * 40)
# Adaugam o valoare
data_curenta.add(2022)
print(f'Data curenta : {data_curenta}')

print("-" * 40)
# Adaugam un tuple
data_curenta.add((7, 8, 9))
print(f'Data curenta : {data_curenta}')

print("-" * 40)
# Stergem un element
data_curenta.remove(2022)
print(f'Data curenta : {data_curenta}')

print("-" * 40)

# print lungime
print(f'Lungimea set data curenta: {len(data_curenta)}')