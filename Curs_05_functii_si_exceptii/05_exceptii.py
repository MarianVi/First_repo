# a = 1/0   # ZeroDivisionError: division by zero
# a = 2 + b     # NameError: name 'b' is not defined

###############################################################

# Aruncarea exceptiilor
x = 2
if x < 0:
    raise Exception('x este mai mic decat 0')

###############################################################

# Tratarea exceptiilor

try:  # Verifica un block de cod pentru exceptii
    print(C)
except:  # Trateaza diferitele tipuri de erori
    print('A aparut o exceptie')

# -------------------------------------------------------------
print('-' * 40)

try:
    print(1 / 0)
except NameError:
    print('Variabila c nu este definita')
except ZeroDivisionError as ex:  # Stocheaza exceptia in variabila ex
    print(f'Eroarea: {ex}')
except:
    print('Alta a fost eroarea')

# ---------------------------------------------------------------
print('-' * 40)

try:
    print('Hello')
except:
    print('Eroare')
else:
    print('Se executa cand nu apare eroare')

# Ramura try, except, else este folosita pentru a rula o bucata de cod daca nu apare eroare in blocul try

# ---------------------------------------------------------------
print('-' * 40)

try:
    print('c')
except:
    print('Eroare')
finally:  # Finally se executa de fiecare data, indiferent daca exista eroare sau nu
    print('Eu ma execut mereu')

####################################################################

'''
try: (blocul try)
    Bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: --> Prinderea tuturor exceptiilor de tipul nume eroare
    Se executa doar daca se prinde nume eroare
except (AltNumeEroare, IncaUnNumeEroare): --> Gruparea mai multor tipuri de exceptii
    Se executa doar daca se prinde una din cele doua erori
except Eroarea4 as ex: --> Stocarea mesajului unei erori intr-o variabila
    Se poate accesa mesajul erorii prin variabila ex
except:
    Se executa pentru orice alt tip de eroare nespecificat
else:
    Se executa doar daca nu se arunca eroare in blocul try
finally:
    Se executa indiferent daca se arunca eroare sau nu
'''
