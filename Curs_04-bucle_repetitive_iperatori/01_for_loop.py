"""
    ITERATORII (bucle repetitive)
- este un obiect care poate fi iterat (parcurs un elemente cate un element, unul cate unul)
(ex: lista, tuple, set, dict, string)
- contin un numar de valori care se pot numara (itera)
"""

fructe = ['mar', 'para', 'banana', 'portocala', 'cireasa']

print(f'fructe : {fructe}')

print('\n','-' * 40)

for fruct in fructe:
    print(fruct, end=' ') # printam pe o singura linie

print('\n','-' * 40) # \n - new line

for fructul_meu in fructe:          # for poate avea else la sfarsit ca si alternativa de incheiere
    print(f'Fructul meu = {fructul_meu}')
else:
    print('Am terminat bucla repetitive for.')                  # (este o particularitate Python)


print('-' * 40)

lista_mixta = ['avocado', 2023, True, 5.66, 'Mihai', (11, 12)]

for elem in lista_mixta:
    if type(elem) is str:
        elem = elem.upper()
        print(elem)
    else:
        print(f'{elem} nu este un string')

print('-' * 40)

# Iteratie la numere :

for numar in range(1, 11, 2):              # in functia range, ultimul numar nu este accesabil
    print(numar)

print('-' * 40)

for numar in range(10, 0, -1):          # parcurgem descrescator
    print(numar, end=' ')

print('\n','-' * 40)

# cea mai simpla iteratie posibila:
for i in range(6):
    print(i, end=' ')