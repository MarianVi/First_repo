# TYPE CASTING
# type (functia type returneaza tipul variabilei sau al datei)

nume_complet, valoare = "Ion Creanga", True
print(type(nume_complet))
print(type(valoare))

# TYPE CASTING - schimbam tipul variabilei
x = 2.712
print(type(x))

y = str(x)
print(type(y))

z = int(x)
print(type(z))

nume = "Eminescu"
nume = int(nume) # ValueError: invalid literal for int() with base 10: 'Eminescu'
print(nume)

