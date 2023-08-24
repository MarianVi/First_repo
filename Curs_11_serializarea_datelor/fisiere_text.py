"""
Serializarea datelor se refera la faptul ca noi dorim persistarea datelor din aplicatie pentru a fi disponibile
    in viitor pentru a putea fi citite sau modificate
"""


# Citire date in mod clasic (se foloseste mereu try - except)
def read_clasic():
    f = open('date.txt', 'r')  # Deschiderea fisierului si retinerea lui in variabila "f"
    try:
        return f.readlines()  # Citim toate datele din fisier
    except Exception as ex:
        print(f'Error: {ex}')
    finally:
        f.close()  # Inchidem fisierul


l = read_clasic()
print(l)

print('-' * 40)


# Citire folosind Context Manager

def read_safe():
    with open('date.txt', 'r') as f:
        return f.readlines()


l = read_safe()
print(l)

print('-' * 40)


# Scriere date in fisier (suprascrie tot continutul anterior)

def write():
    with open('date.txt', 'w') as f:
        f.writelines(['1\n', 'abc\n', '1 2 3\n'])


write()

# Adaugare date in fisier

def append():
    with open('date.txt', 'a') as f:
        f.writelines(['banane\n', 'hocus pocus'])

append()