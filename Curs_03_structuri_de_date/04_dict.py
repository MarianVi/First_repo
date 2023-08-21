# DICT - Dictionarul
"""
- Dictionarul este o colectie de date de tip cheie - valoare
- este MUTABLE
- cheile (keys) sunt unice
- valorile (values) se pot repeta
- keys trebuie sa fie IMMUTABLE (doar de tip: int, str, tuple)
"""

# Initializare dictionar
persoana = {
    'nume': 'Stefan',
    'prenume': 'Gheorghiu',
    'varsta': 47
}

print(f'Persoana = {persoana}')

print('-' * 40)

# Adaugarea unui element in dictionar
persoana['initiala_tatalui'] = 'P'

print(f'Persoana = {persoana}')

print('-' * 40)

# Accesarea unui element existent / non-existent => eroare (ca si la set)
print(f'Valoarea cheii unui elem : {persoana["varsta"]}')
# print(f'Valoarea unui elem : {persoana["var"]}')          #KeyError: 'var'

print('-' * 40)

# Lungimea dictionarului
lungime_dict = len(persoana)
print(f'Lungime dict = {lungime_dict}')

print('-' * 40)

# Stergerea unui element
persoana.pop('initiala_tatalui')
print(f'Persoana = {persoana}')

print('-' * 40)

# Modificarea unui element (se foloseste cheia)
persoana['initiala_tatalui'] = 'Y'
print(f'Persoana = {persoana}')